# Docker

[Docker](https://hub.docker.com/r/mbootgithub/whoisdomain)

 * docker pull mbootgithub/whoisdomain:latest
 * docker run mbootgithub/whoisdomain -V # show version
 * docker run mbootgithub/whoisdomain -d google.com # run one domain
 * docker run mbootgithub/whoisdomain -a # run all tld
 * docker run mbootgithub/whoisdomain -d google.com -j | jq -r . # run one domains , output in json and reformat with jq
 * docker run mbootgithub/whoisdomain -d google.com -j | jq -r '.expiration_date' # output only expire date
 * docker run mbootgithub/whoisdomain -d google.com -j | jq -r '[ .expiration_date, .creation_date ]
