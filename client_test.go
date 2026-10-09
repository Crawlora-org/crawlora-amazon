package amazon

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
	"time"
)

func TestGeneratedClientRequestAndAllowlist(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodGet {
			t.Errorf("method = %s, want GET", r.Method)
		}
		if r.Header.Get("x-api-key") != "test-key" {
			t.Errorf("x-api-key = %q", r.Header.Get("x-api-key"))
		}
		if r.URL.EscapedPath() != "/api/v1/amazon/product/folder%2Fitem" {
			t.Errorf("escaped path = %q", r.URL.EscapedPath())
		}
		if "language" != "" {
			if got := r.URL.Query().Get("language"); got != "en_US" {
				t.Errorf("query value = %q", got)
			}
			if false && len(r.URL.Query()["language"]) != 2 {
				t.Errorf("array query values = %#v", r.URL.Query()["language"])
			}
		}
		if "language" != "" && !strings.Contains(r.URL.RawQuery, "language=en_US") {
			t.Errorf("raw query = %q, missing encoded parameter %s", r.URL.RawQuery, "language=en_US")
		}
		w.Header().Set("Content-Type", "application/json")
		_ = json.NewEncoder(w).Encode(map[string]any{"ok": true})
	}))
	defer server.Close()
	client := NewClient("test-key")
	client.BaseURL = server.URL + "/api/v1"
	client.HTTPClient = server.Client()
	got, err := client.Call(context.Background(), "amazon-product", Params{"asin": "folder/item", "language": "en_US", "currency": "USD"})
	if err != nil {
		t.Fatal(err)
	}
	if got.(map[string]any)["ok"] != true {
		t.Fatalf("JSON result = %#v", got)
	}
	if OperationCount != 5 || len(OperationIDs()) != OperationCount {
		t.Fatalf("operation count = %d IDs=%d", OperationCount, len(OperationIDs()))
	}
	if _, err := client.Call(context.Background(), "unselected-operation", nil); err == nil || !strings.Contains(err.Error(), "unknown") {
		t.Fatalf("unselected operation error = %v", err)
	}
	if "language" != "" {
		if _, err := client.Call(context.Background(), "amazon-product", Params{"asin": "folder/item", "language": "__invalid_enum__", "currency": "__invalid_enum__"}); err == nil || !strings.Contains(err.Error(), "invalid value") {
			t.Fatalf("invalid enum error = %v", err)
		}
	}
	if err := client.Close(); err != nil {
		t.Fatal(err)
	}
}

func TestGeneratedClientTextResponse(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "text/plain; charset=utf-8")
		_, _ = w.Write([]byte("feed text"))
	}))
	defer server.Close()
	client := NewClient("key")
	client.BaseURL = server.URL + "/api/v1"
	client.HTTPClient = server.Client()
	got, err := client.Call(context.Background(), "amazon-product", Params{"asin": "folder/item", "language": "en_US", "currency": "USD", "responseType": "text"})
	if err != nil {
		t.Fatal(err)
	}
	if got != "feed text" {
		t.Fatalf("text result = %#v", got)
	}
}

func TestGeneratedClientErrorsAndTimeout(t *testing.T) {
	t.Run("HTTP error", func(t *testing.T) {
		server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, _ *http.Request) {
			http.Error(w, "upstream unavailable", http.StatusBadGateway)
		}))
		defer server.Close()
		client := NewClient("key")
		client.BaseURL = server.URL + "/api/v1"
		client.HTTPClient = server.Client()
		_, err := client.Call(context.Background(), "amazon-product", Params{"asin": "folder/item", "language": "en_US", "currency": "USD"})
		if err == nil || !strings.Contains(err.Error(), "502") {
			t.Fatalf("HTTP error = %v", err)
		}
	})

	t.Run("timeout", func(t *testing.T) {
		server := httptest.NewServer(http.HandlerFunc(func(_ http.ResponseWriter, r *http.Request) {
			<-r.Context().Done()
		}))
		defer server.Close()
		client := NewClient("key")
		client.BaseURL = server.URL + "/api/v1"
		client.HTTPClient = server.Client()
		client.Timeout = 10 * time.Millisecond
		_, err := client.Call(context.Background(), "amazon-product", Params{"asin": "folder/item", "language": "en_US", "currency": "USD"})
		if err == nil {
			t.Fatal("expected request timeout")
		}
	})
}

func ExampleClient_Call() {
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, _ *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		_, _ = w.Write([]byte(`{"ok":true}`))
	}))
	defer server.Close()

	client := NewClient("your-crawlora-api-key")
	client.BaseURL = server.URL + "/api/v1"
	client.HTTPClient = server.Client()
	result, err := client.Call(context.Background(), "amazon-charts", Params{"chart": "best_sellers", "department": "sample"})
	if err != nil {
		panic(err)
	}
	fmt.Println(result.(map[string]any)["ok"])
	// Output: true
}
