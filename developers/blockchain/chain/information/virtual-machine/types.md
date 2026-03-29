# Types

The Phantasma VM uses a small fixed set of runtime value types. These types appear in:

- ABI signatures
- register values
- stack values
- serialized VM objects
- constructor-style interops such as `Address()`, `Hash()`, and `Timestamp()`

## Runtime Types

| Type | Internal Value | Typical Use | Notes |
| --- | ---: | --- | --- |
| `None` | `0` | empty / uninitialized value | Equivalent to a VM-level null or empty slot. |
| `Struct` | `1` | compound values, arrays, maps | Used for dynamic object shapes and collection-like results. |
| `Bytes` | `2` | raw binary payloads | Common for script bytes, ABI bytes, ROM, RAM, storage payloads, and serialized values. |
| `Number` | `3` | integer arithmetic | Backed by big integers, not fixed-width contract integers. |
| `String` | `4` | text values | Used for symbols, contract names, field names, and method names. |
| `Timestamp` | `5` | date/time values | Exposed as a distinct VM type and also convertible through numeric paths. |
| `Bool` | `6` | true / false | Used heavily in interop results and guard conditions. |
| `Enum` | `7` | enum-like values | Common for flags, trigger kinds, and typed control values. |
| `Object` | `8` | runtime-native objects | In current Carbon practice this is mainly used for values such as `Address`, `Hash`, or execution-context objects. |

## Developer Notes

### `Number`

`Number` is the default arithmetic type. You should think of it as an arbitrary-size integer value, not a 32-bit or 64-bit integer.

### `Struct`

`Struct` is the general-purpose compound container. The runtime also uses struct-shaped VM objects to return array-like and map-like results, for example from:

- `Runtime.GetOwnerships`
- `Runtime.ReadToken`
- `Runtime.ReadInfusions`
- `Map.Keys`

### `Object`

`Object` deserves special attention.

For contract authors, it is best treated as a runtime-native wrapper type rather than a generic user-defined object model. In current Carbon code it is mainly used for:

- addresses
- hashes
- execution contexts

That is why the constructor-style interops return object-backed values:

- `Address()`
- `Hash()`
- `Timestamp()` does not return `Object`; it returns the typed timestamp value directly

In other words, `Object` exists, but developers should not build contract design around arbitrary host reflection or arbitrary native object serialization.

## Default Or Missing Values

Some interops return typed default values when a storage slot is missing. For example:

- `Data.Get`
- `Map.Get`
- `List.Get`

When that happens, the runtime uses the requested VM type to decide what default shape to return. This is why many storage getters ask for the expected type explicitly.
