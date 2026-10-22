use crawlora_amazon::{AmazonSearchParams, Client, ModelAmazonSearchResponseDoc};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .amazon
        .search(AmazonSearchParams {
            k: Some("wireless headphones".to_owned()),
            ..Default::default()
        })
        .await?;
    let data: ModelAmazonSearchResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
