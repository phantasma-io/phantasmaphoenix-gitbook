# Types

The registers for the Phantasma VM at each moment in execution time can hold values for one of the following types.

| Type      | Serialization Internal Value | Description                                                                                                             | Available casts                |
| --------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| None      | 0                            | Almost equivalent to a "null" value. Represents an uninitialized value.                                                 | -                              |
| Struct    | 1                            | Represents a complex object and can be used for structs, arrays and maps.                                               | -                              |
| Bytes     | 2                            | A variable length array of bytes.                                                                                       | Can be cast to: Number, String |
| Number    | 3                            | a 256-bit integer number.                                                                                               | Can be cast to: String         |
| String    | 4                            | A variable length string of characters.                                                                                 | -                              |
| Timestamp | 5                            | A 32-bit Unix based timestamp.                                                                                          | Can be cast to: Number         |
| Bool      | 6                            | A boolean object (true/false).                                                                                          | Can be cast to: Number, String |
| Enum      | 7                            | An enumerable value.                                                                                                    | Can be cast to: Number         |
| Object    | 8                            | Used to represent a complex object (non-native to the VM, eg: a C# class instance). In most cases cannot be serialized. | -                              |

##
