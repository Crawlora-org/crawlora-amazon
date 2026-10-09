import { AmazonClient } from "../src/index.js";

const client = new AmazonClient({ apiKey: "test-key" });
void client.charts({"chart": "best_sellers", "department": "sample"});
void client.request("amazon-charts", {"chart": "best_sellers", "department": "sample"});
const streamResponse: Promise<Response> = client.request("amazon-charts", {"chart": "best_sellers", "department": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("amazon-charts", {"chart": "best_sellers", "department": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.charts({"chart": "best_sellers", "department": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("amazon-charts", {"chart": "best_sellers", "department": "sample", "node": "sample", "page": 1}, { responseType: "text" });
const rawText: Promise<string> = client.request("amazon-charts", {"chart": "best_sellers", "department": "sample"}, { responseType: "text" });
void rawText;



// @ts-expect-error The selected operation requires its documented params.
void client.charts();
