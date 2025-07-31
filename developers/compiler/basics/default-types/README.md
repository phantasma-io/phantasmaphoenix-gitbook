# Default types

{% hint style="info" %}
Different data types are recognized by the compiler.
{% endhint %}

| Type           | Example                                                           |                                                                                |
| -------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Number         | 123                                                               | Integer values only. Negative values supported. Number must fit into 256 bits. |
| Decimal        | 0.123                                                             | Where X is the number of maximum decimal places.                               |
| Bool           | false                                                             | Either true or false                                                           |
| String         | "hello"                                                           | Single line only.                                                              |
| Timestamp      |                                                                   | No literal support for this type, use either Time.now or Time.unix             |
| Byte array     | 0xFAFAFA2423424                                                   | In hexadecimal format, starting with 0x                                        |
| Address        | @P2K6p3VzyRhxqHE2KcNV2B3QjVrv5ekvWPZLevteDoBQTzA or @null         |                                                                                |
| Hash           | #E3FE7BB73996CF7057913BD916F1B07AC0EAB4916DF3BCBDC221829F5CBEA9AF | Must be hexadecimal number with 256 bits                                       |
| Compiler macro | $SOMETHING                                                        |                                                                                |

