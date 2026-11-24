---
title: "Default types"
linkTitle: "Default Types"
weight: 90
---

> [!NOTE]
> Different data types are recognized by the compiler.

| Type           | Example                                                           |                                                                                |
| -------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Number         | 123                                                               | Integer values only, negative values included. The VM `Number` is a big integer. |
| Decimal        | 0.123                                                             | Declared as `decimal<N>`, where N is the number of decimal places; stored as a `Number` in fixed point. |
| Bool           | false                                                             | Either true or false                                                           |
| String         | "hello"                                                           | Single line only.                                                              |
| Timestamp      |                                                                   | No literal support for this type, use either Time.now or Time.unix             |
| Byte array     | 0xFAFAFA2423424                                                   | In hexadecimal format, starting with 0x                                        |
| Address        | @P2K6p3VzyRhxqHE2KcNV2B3QjVrv5ekvWPZLevteDoBQTzA or @null         |                                                                                |
| Hash           | #E3FE7BB73996CF7057913BD916F1B07AC0EAB4916DF3BCBDC221829F5CBEA9AF | Must be hexadecimal number with 256 bits                                       |
| Compiler macro | $SOMETHING                                                        |                                                                                |
