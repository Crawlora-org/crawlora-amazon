require_relative "lib/crawlora/amazon/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-amazon"
  spec.version = Crawlora::Amazon::VERSION
  spec.summary = "Amazon client for the Crawlora hosted API"
  spec.description = "Credential-free Amazon API access through Crawlora's hosted service."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=amazon-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-amazon", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-amazon/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
