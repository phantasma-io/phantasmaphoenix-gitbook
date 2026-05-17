# C++ SDK Schemas And Metadata

Carbon NFT schemas live in `Carbon/Contracts/TokenSchemas.h` and
`Carbon/Contracts/Token.h`. `TokenSchemas` separates series metadata, NFT ROM,
and NFT RAM.

## Standard Fields

Standard display metadata fields are:

| Field | Type |
| ----- | ---- |
| `name` | string |
| `description` | string |
| `imageURL` | string |
| `infoURL` | string |
| `royalties` | signed 32-bit integer |

The SDK adds standard system fields such as `_i`, `mode`, and `rom` where the
chain expects them. Do not include chain-owned fields in public deterministic
mint metadata.

## Builders And Structures

| API | Purpose |
| --- | ------- |
| `TokenInfo` | Token definition serialized in create-token calls. |
| `SeriesInfo` | NFT series definition serialized in create-series calls. |
| `TokenInfoOwned`, `SeriesInfoOwned` | Owned storage wrappers for view-based structures. |
| `TokenMetadataBuilder` | Token-level metadata bytes. |
| `TokenSchemas` | Series metadata, ROM, and RAM schema container. |
| `NftMintInfo`, `PhantasmaNftMintInfo` | Direct and deterministic mint records. |
| `PhantasmaNftMintResult` | Deterministic mint result row. |

View structures use `ByteView` fields. Keep the backing storage alive for as
long as the message envelope references it.
