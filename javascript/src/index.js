import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class AmazonClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-amazon-js/0.1.1" });
    this["charts"] = (...args) => this.request("amazon-charts", ...args);
    this["chartsCategories"] = (...args) => this.request("amazon-charts-categories", ...args);
    this["product"] = (...args) => this.request("amazon-product", ...args);
    this["search"] = (...args) => this.request("amazon-search", ...args);
    this["suggest"] = (...args) => this.request("amazon-suggest", ...args);
  }
}

export { AmazonClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.1";
export default AmazonClient;
