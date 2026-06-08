Just like retrieving data with GET requests, we can send data to an API server using the .post() method.

The post() method requires a URL and typically includes headers and data as arguments. The principle is that your data will be sent to the API endpoint, and the server will process it.

The headers and data are passed as dictionaries with their key-value pairs.

Note:
#### Headers typically include <b>metadata</b> about your request (like content type)
#### The json parameter automatically converts your Python dictionary to JSON format
#### Some APIs require <b>authentication</b> via API keys in the headers

or simply .post() contains 3 things:
    -> URL
    -> headers : contains content-types
    ->json params
