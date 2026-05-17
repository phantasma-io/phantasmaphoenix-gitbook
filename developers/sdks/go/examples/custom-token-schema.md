# Go SDK Example: Custom Token Schema

```go
package main

import (
    "fmt"
    "log"

    "github.com/phantasma-io/phantasma-sdk-go/pkg/carbon"
)

func main() {
    schemas, err := carbon.TokenSchemasFromJSON(`{
      "seriesMetadata": [
        {"name": "name", "type": "String"},
        {"name": "description", "type": "String"},
        {"name": "imageURL", "type": "String"},
        {"name": "infoURL", "type": "String"},
        {"name": "royalties", "type": "Int32"}
      ],
      "rom": [
        {"name": "artist", "type": "String"},
        {"name": "album", "type": "String"}
      ],
      "ram": [
        {"name": "level", "type": "Int32"}
      ]
    }`)
    if err != nil {
        log.Fatal(err)
    }

    if err := carbon.VerifyTokenSchemas(schemas); err != nil {
        log.Fatal(err)
    }

    fmt.Println(carbon.SerializeTokenSchemasHex(schemas))
}
```

The parser expects JSON object sections named `seriesMetadata`, `rom`, and
`ram`. Each section must be an array of `{name, type}` objects.
