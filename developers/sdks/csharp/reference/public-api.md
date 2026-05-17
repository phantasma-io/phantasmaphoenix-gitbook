# C# SDK Public API Inventory

This page lists public classes, methods, functions, enum values, fields, and
constants from the cited source baseline. Use it to check exact names when
working with lower-level SDK APIs.

Source baseline:

| Item | Value |
| ---- | ----- |
| Source repo | `phantasmaphoenix-sdk-cs` |
| Source commit | `820680b38e67109b7f94e1d26058d6933f758b26` |
| Scope | public C# symbols in PhantasmaPhoenix library projects, excluding tests and examples |

## PhantasmaPhoenix.Core.ISerializable

Source: `PhantasmaPhoenix.Core/src/Abstractions/ISerializable.cs`

### Declarations

```csharp
public interface ISerializable
```

### Methods

```csharp
public void SerializeData(BinaryWriter writer);
```

```csharp
public void UnserializeData(BinaryReader reader);
```

## PhantasmaPhoenix.Core.ByteArrayComparer

Source: `PhantasmaPhoenix.Core/src/ByteArrayComparer.cs`

### Declarations

```csharp
public class ByteArrayComparer : IEqualityComparer<byte[]>, IEqualityComparer, IComparer<byte[]>
```

## PhantasmaPhoenix.Core.ByteArrayUtils

Source: `PhantasmaPhoenix.Core/src/ByteArrayUtils.cs`

### Declarations

```csharp
public static class ByteArrayUtils
```

### Methods

```csharp
public static bool CompareBytes(this byte[] left, byte[] right)
```

```csharp
public static byte[] ConcatBytes(byte source1, byte[] source2)
```

```csharp
public static byte[] ConcatBytes(byte[] source1, byte[] source2)
```

```csharp
public static byte[] RangeBytes(this byte[] data, int index, int length)
```

```csharp
public static byte[] ReverseBytes(byte[] source)
```

```csharp
public static byte[]? DupBytes(byte[] src)
```

```csharp
public static int SearchBytes(this byte[] haystack, byte[] needle)
```

```csharp
public static void CopyBytes(byte[] src, int spos, byte[] dst, int dpos, int len)
```

## PhantasmaPhoenix.Core.ChainException

Source: `PhantasmaPhoenix.Core/src/Exceptions/ChainException.cs`

### Declarations

```csharp
public class ChainException : Exception
```

### Methods

```csharp
public ChainException(string msg) : base(msg)
```

## PhantasmaPhoenix.Core.Extensions.ByteArrayExtensions

Source: `PhantasmaPhoenix.Core/src/Extensions/ByteArrayExtensions.cs`

### Declarations

```csharp
public static class ByteArrayExtensions
```

### Methods

```csharp
public static string AsString(this byte[] source)
```

```csharp
public static uint ToUInt32(this byte[] value, int startIndex)
```

## PhantasmaPhoenix.Core.Extensions.DoubleExtensions

Source: `PhantasmaPhoenix.Core/src/Extensions/DoubleExtensions.cs`

### Declarations

```csharp
public static class DoubleExtensions
```

### Methods

```csharp
public static bool ApproximatelyEquals(this double d, double val, double range)
```

## PhantasmaPhoenix.Core.Extensions.IDictionaryExtensions

Source: `PhantasmaPhoenix.Core/src/Extensions/IDictionaryExtensions.cs`

### Declarations

```csharp
public static class IDictionaryExtensions
```

### Methods

```csharp
public static void Merge<K, V>(this IDictionary<K, V> target, IDictionary<K, V> source)
```

## PhantasmaPhoenix.Core.Extensions.IEnumerableExtensions

Source: `PhantasmaPhoenix.Core/src/Extensions/IEnumerableExtensions.cs`

### Declarations

```csharp
public static class IEnumerableExtensions
```

### Methods

```csharp
public static IEnumerable<T> ExceptBy<T, TKey>(this IEnumerable<T> src, IEnumerable<T> items, Func<T, TKey> keySelector)
```

```csharp
public static IEnumerable<T> ExceptBy<T, TKey>(this IEnumerable<T> src, T item, Func<T, TKey> keySelector)
```

```csharp
public static bool None<TSource>(this IEnumerable<TSource> source)
```

```csharp
public static bool None<TSource>(this IEnumerable<TSource> source, Func<TSource, bool> predicate)
```

```csharp
public static double StdDev(this IEnumerable<double> values)
```

```csharp
public static void ForEach<T>(this IEnumerable collection, Action<T> action)
```

```csharp
public static void ForEach<T>(this IEnumerable<T> collection, Action<T> action)
```

```csharp
public static void ForEachWithIndex<T>(this IEnumerable<T> collection, Action<T, int> action)
```

## PhantasmaPhoenix.Core.Extensions.IntExtensions

Source: `PhantasmaPhoenix.Core/src/Extensions/IntExtensions.cs`

### Declarations

```csharp
public static class IntExtensions
```

### Methods

```csharp
public static IEnumerable<int> Range(this int n)
```

```csharp
public static void ForEach(this int n, Action action)
```

```csharp
public static void ForEach(this int n, Action<int> action)
```

## PhantasmaPhoenix.Core.Extensions.JsonDocumentExtensions

Source: `PhantasmaPhoenix.Core/src/Extensions/JsonDocumentExtensions.cs`

### Declarations

```csharp
public static class JsonDocumentExtensions
```

### Methods

```csharp
public static string ToJsonString(this JToken token)
```

## PhantasmaPhoenix.Core.Extensions.ListExtensions

Source: `PhantasmaPhoenix.Core/src/Extensions/ListExtensions.cs`

### Declarations

```csharp
public static class ListExtensions
```

### Methods

```csharp
public static bool ContainsBy<T, TKey>(this List<T> list, T item, Func<T, TKey> keySelector)
```

```csharp
public static void AddDistinct<T>(this List<T> list, T item)
```

```csharp
public static void AddDistinctBy<T, TKey>(this List<T> list, T item, Func<T, TKey> keySelector)
```

```csharp
public static void AddMaximum<T>(this List<T> list, T item, int max)
```

```csharp
public static void AddRangeDistinctBy<T>(this List<T> target, IEnumerable<T> src, Func<T, T, bool> equalityComparer)
```

```csharp
public static void MoveToTail<T>(this List<T> list, T item, Predicate<T> pred)
```

```csharp
public static void RemoveRange<T>(this List<T> target, List<T> src)
```

```csharp
public static void RemoveRange<T>(this List<T> target, List<T> src, Func<T, T, bool> equalityComparer)
```

```csharp
public static void Shuffle<T>(this IList<T> list)
```

## PhantasmaPhoenix.Core.Extensions.StringExtensions

Source: `PhantasmaPhoenix.Core/src/Extensions/StringExtensions.cs`

### Declarations

```csharp
public static class StringExtensions
```

### Methods

```csharp
public static byte[] AsByteArray(this string source)
```

```csharp
public static byte[]? FromHex(this string? value) //todo return not null if value not null
```

```csharp
public static string ToHex(this byte[] value)
```

```csharp
public static string ToHex(this byte[] value, int offset, int count)
```

## PhantasmaPhoenix.Core.Extensions.TypeExtensions

Source: `PhantasmaPhoenix.Core/src/Extensions/TypeExtensions.cs`

### Declarations

```csharp
public static class TypeExtensions
```

### Methods

```csharp
public static bool IsStructOrClass(this Type type)
```

## PhantasmaPhoenix.Core.HexByteArrayJsonConverter

Source: `PhantasmaPhoenix.Core/src/HexByteArrayJsonConverter.cs`

### Declarations

```csharp
public class HexByteArrayJsonConverter : JsonConverter<byte[]>
```

### Methods

```csharp
public HexByteArrayJsonConverter() { }
```

```csharp
public override byte[] ReadJson(JsonReader reader, Type objectType, byte[]? existingValue, bool hasExistingValue, JsonSerializer serializer)
```

```csharp
public override void WriteJson(JsonWriter writer, byte[]? value, JsonSerializer serializer)
```

## PhantasmaPhoenix.Core.Compression

Source: `PhantasmaPhoenix.Core/src/Serialization/Compression.cs`

### Declarations

```csharp
public static class Compression
```

### Methods

```csharp
public static byte[] Compress(byte[] data)
```

```csharp
public static byte[] Decompress(byte[] data)
```

## PhantasmaPhoenix.Core.CustomSerializer

Source: `PhantasmaPhoenix.Core/src/Serialization/CustomSerializer.cs`

### Declarations

```csharp
public struct CustomSerializer
```

### Methods

```csharp
public CustomSerializer(CustomReader reader, CustomWriter writer)
```

```csharp
public readonly CustomReader Read;
```

```csharp
public readonly CustomWriter Write;
```

## PhantasmaPhoenix.Core.Extensions.BigIntegerExtension

Source: `PhantasmaPhoenix.Core/src/Serialization/Extensions/BigIntegerExtensions.cs`

### Declarations

```csharp
public static class BigIntegerExtension
```

### Methods

```csharp
public static BigInteger HexToBigInteger(this string a)
```

```csharp
public static BigInteger Mod(this BigInteger a, BigInteger b)
```

```csharp
public static BigInteger ModInverse(this BigInteger a, BigInteger n)
```

```csharp
public static System.Numerics.BigInteger AsBigInteger(this byte[] source)
```

```csharp
public static bool IsParsable(this string val)
```

```csharp
public static bool TestBit(this BigInteger a, int index)
```

```csharp
public static byte[] AsByteArray(this BigInteger source)
```

```csharp
public static byte[] ToSignedByteArray(this BigInteger a)
```

```csharp
public static byte[] ToUnsignedByteArray(this BigInteger a)
```

```csharp
public static int GetBitLength(this BigInteger a)
```

```csharp
public static int GetLowestSetBit(this BigInteger a)
```

## PhantasmaPhoenix.Core.Extensions.BinaryIoBasicTypesExtensions

Source: `PhantasmaPhoenix.Core/src/Serialization/Extensions/BinaryIoBasicTypesExtensions.cs`

### Declarations

```csharp
public static class BinaryIoBasicTypesExtensions
```

### Methods

```csharp
public static BigInteger ReadBigInteger(this BinaryReader reader)
```

```csharp
public static T ReadSerializable<T>(this BinaryReader reader, int max = 0x1000000) where T : ISerializable, new()
```

```csharp
public static T[] ReadSerializableArray<T>(this BinaryReader reader, int max = 0x1000000) where T : ISerializable, new()
```

```csharp
public static Timestamp ReadTimestamp(this BinaryReader reader)
```

```csharp
public static byte[] ReadByteArray(this BinaryReader reader)
```

```csharp
public static byte[] ReadFixedBytes(this BinaryReader reader, int size)
```

```csharp
public static byte[] ReadVarBytes(this BinaryReader reader, int max = 0x1000000)
```

```csharp
public static byte[] ToArray(this ISerializable value)
```

```csharp
public static int GetVarSize(int value)
```

```csharp
public static int GetVarSize(this string value)
```

```csharp
public static int GetVarSize<T>(this IReadOnlyCollection<T> value)
```

```csharp
public static string ReadVarString(this BinaryReader reader, int max)
```

```csharp
public static string? ReadVarString(this BinaryReader reader)
```

```csharp
public static ulong ReadVarInt(this BinaryReader reader, ulong max = ulong.MaxValue)
```

```csharp
public static void Write(this BinaryWriter writer, ISerializable value)
```

```csharp
public static void Write<T>(this BinaryWriter writer, IReadOnlyCollection<T> value) where T : ISerializable
```

```csharp
public static void WriteBigInteger(this BinaryWriter writer, BigInteger n)
```

```csharp
public static void WriteByteArray(this BinaryWriter writer, byte[] bytes)
```

```csharp
public static void WriteNullableArray<T>(this BinaryWriter writer, T[] value) where T : class, ISerializable
```

```csharp
public static void WriteTimestamp(this BinaryWriter writer, Timestamp timestamp)
```

```csharp
public static void WriteVarBytes(this BinaryWriter writer, ReadOnlySpan<byte> value)
```

```csharp
public static void WriteVarInt(this BinaryWriter writer, long value)
```

```csharp
public static void WriteVarString(this BinaryWriter writer, string text)
```

## PhantasmaPhoenix.Core.Serialization

Source: `PhantasmaPhoenix.Core/src/Serialization/Serialization.cs`

### Declarations

```csharp
public static class Serialization
```

### Methods

```csharp
public static ISerializable AsSerializable(this byte[] value, Type type)
```

```csharp
public static T? Unserialize<T>(BinaryReader reader)
```

```csharp
public static T? Unserialize<T>(byte[] bytes)
```

```csharp
public static byte[] Serialize(this object obj)
```

```csharp
public static object? Unserialize(BinaryReader reader, Type type)
```

```csharp
public static object? Unserialize(byte[] bytes, Type type)
```

```csharp
public static void RegisterType<T>(CustomReader reader, CustomWriter writer)
```

```csharp
public static void Serialize(BinaryWriter writer, object obj)
```

```csharp
public static void Serialize(BinaryWriter writer, object obj, Type type)
```

## PhantasmaPhoenix.Core.StructuralEqualityComparer

Source: `PhantasmaPhoenix.Core/src/StructuralEqualityComparer.cs`

### Declarations

```csharp
public class StructuralEqualityComparer<T> : IEqualityComparer<T>
```

### Methods

```csharp
public bool Equals(T? x, T? y)
```

```csharp
public int GetHashCode(T obj)
```

```csharp
public static StructuralEqualityComparer<T> Default
```

## PhantasmaPhoenix.Core.Timestamp

Source: `PhantasmaPhoenix.Core/src/Structures/Timestamp.cs`

### Declarations

```csharp
public struct Timestamp : IComparable<Timestamp>
```

### Methods

```csharp
public Timestamp(BigInteger value)
```

```csharp
public Timestamp(string value)
```

```csharp
public Timestamp(uint value)
```

```csharp
public int CompareTo(Timestamp other)
```

```csharp
public int GetSize()
```

```csharp
public override bool Equals(object? obj)
```

```csharp
public override int GetHashCode()
```

```csharp
public override string ToString()
```

```csharp
public readonly static Timestamp Null = new Timestamp(0);
```

```csharp
public readonly uint Value;
```

```csharp
public static Timestamp Now => DateTime.UtcNow;
```

```csharp
public static bool operator !=(Timestamp A, Timestamp B)
```

```csharp
public static bool operator <(Timestamp A, Timestamp B)
```

```csharp
public static bool operator <=(Timestamp A, Timestamp B)
```

```csharp
public static bool operator ==(Timestamp A, Timestamp B)
```

```csharp
public static bool operator >(Timestamp A, Timestamp B)
```

```csharp
public static bool operator >=(Timestamp A, Timestamp B)
```

```csharp
public static implicit operator DateTime(Timestamp timestamp)
```

```csharp
public static implicit operator Timestamp(DateTime time)
```

```csharp
public static implicit operator Timestamp(uint ticks)
```

```csharp
public static uint operator +(Timestamp A, TimeSpan B)
```

```csharp
public static uint operator -(Timestamp A, TimeSpan B)
```

```csharp
public static uint operator -(Timestamp A, Timestamp B)
```

```csharp
public string ToString(string format)
```

## PhantasmaPhoenix.Core.Throw

Source: `PhantasmaPhoenix.Core/src/Throw.cs`

### Declarations

```csharp
public static class Throw
```

### Methods

```csharp
public static Exception? ExpandInnerExceptions(this Exception? ex)
```

```csharp
public static void Assert( #if NET6_0_OR_GREATER #endif bool condition, string message = "assertion failure")
```

```csharp
public static void If( #if NET6_0_OR_GREATER #endif bool constraint, string constraintName)
```

```csharp
public static void If(Func<bool> lambda, string constraintName)
```

```csharp
public static void IfEmpty(string argumentValue, string argumentName)
```

```csharp
public static void IfEmpty<T>(IEnumerable<T> argumentValue, string argumentName)
```

```csharp
public static void IfHasNull<T>(ICollection<T> argumentValue, string argumentName)
```

```csharp
public static void IfInRange(int argumentValue, int startRange, int endRange, string argumentName)
```

```csharp
public static void IfNot( #if NET6_0_OR_GREATER #endif bool constraint, string constraintName)
```

```csharp
public static void IfNot(Func<bool> lambda, string constraintName)
```

```csharp
public static void IfNull(object? argumentValue, string argumentName)
```

```csharp
public static void IfNull<T>(T? argumentValue, string argumentName) where T : struct
```

```csharp
public static void IfNullOrEmpty(ICollection argumentValue, string argumentName)
```

```csharp
public static void IfNullOrEmpty(string argumentValue, string argumentName)
```

```csharp
public static void IfOutOfRange(Enum argumentValue, string argumentName)
```

```csharp
public static void IfOutOfRange(int argumentValue, int startRange, int endRange, string argumentName)
```

## PhantasmaPhoenix.Core.Tools.NamedStopwatch

Source: `PhantasmaPhoenix.Core/src/Tools/NamedStopwatch.cs`

### Declarations

```csharp
public sealed class NamedStopwatch
```

### Methods

```csharp
public NamedStopwatch( string name )
```

```csharp
public bool HasName => !string.IsNullOrEmpty(Name);
```

```csharp
public long ElapsedMilliseconds => _stopwatch.ElapsedMilliseconds;
```

```csharp
public readonly string Name;
```

```csharp
public static string StopwatchesToString(List<NamedStopwatch> stopwatches, Stopwatch totalStopwatch)
```

```csharp
public static void Start( ref List<NamedStopwatch> stopwatches, string name )
```

```csharp
public static void Stop( List<NamedStopwatch> stopwatches, string name )
```

```csharp
public string GetPrefixedName( string prefix )
```

```csharp
public void Reset()
```

```csharp
public void Start()
```

```csharp
public void Stop()
```

## PhantasmaPhoenix.Core.Tools.NamedStopwatchSet

Source: `PhantasmaPhoenix.Core/src/Tools/NamedStopwatchSet.cs`

### Declarations

```csharp
public sealed class NamedStopwatchSet
```

### Methods

```csharp
public NamedStopwatchSet(bool enabled, bool startTotal = true)
```

```csharp
public long ElapsedMilliseconds => _totalStopwatch?.ElapsedMilliseconds ?? 0;
```

```csharp
public override string ToString()
```

```csharp
public string? GetReportIfReady(string messagePrefix)
```

```csharp
public void Configure(uint reportFrequencyLimitInSeconds, uint reportMinElapsedLimitInMilliseconds = 100)
```

```csharp
public void Reset(bool resetTotal = true)
```

```csharp
public void Start(string name)
```

```csharp
public void Stop()
```

```csharp
public void Stop(string name)
```

```csharp
public void StopAll(bool stopTotal = false)
```

```csharp
public void TotalStart()
```

```csharp
public void TotalStop()
```

## PhantasmaPhoenix.Core.Tools.ProfileSession

Source: `PhantasmaPhoenix.Core/src/Tools/ProfileMarker.cs`

### Declarations

```csharp
public class ProfileSession : IDisposable
```

### Methods

```csharp
public ProfileMarker(string name)
```

```csharp
public ProfileMarker(string name, ProfileMarker parent)
```

```csharp
public ProfileSession(System.IO.Stream o)
```

```csharp
public int parentIdx;
```

```csharp
public long end;
```

```csharp
public long start;
```

```csharp
public static ProfileSession CurrentSession;
```

```csharp
public string name;
```

```csharp
public struct ProfileMarker : IDisposable
```

```csharp
public void Pop(string name)
```

```csharp
public void Push(string name)
```

```csharp
public void Stop()
```

## PhantasmaPhoenix.Core.Tools.TaskLogger

Source: `PhantasmaPhoenix.Core/src/Tools/TaskLogger.cs`

### Declarations

```csharp
public static class TaskLogger
```

### Methods

```csharp
public static IReadOnlyDictionary<string, int> GetSnapshot()
```

```csharp
public static Task RunLogged(string name, Func<Task> func)
```

```csharp
public static void Initialize(ILogger logger, TimeSpan interval, CancellationToken? ct = default)
```

```csharp
public static void RunFireAndForget(string name, Func<Task> func)
```

## PhantasmaPhoenix.Core.UnitConversion

Source: `PhantasmaPhoenix.Core/src/UnitConversion.cs`

### Declarations

```csharp
public static class UnitConversion
```

### Methods

```csharp
public static BigInteger ConvertDecimals(BigInteger value, uint decimalFrom, uint decimalTo)
```

```csharp
public static BigInteger GetUnitValue(uint decimals)
```

```csharp
public static BigInteger ToBigInteger(decimal n, uint units)
```

```csharp
public static decimal ToDecimal(BigInteger value, uint tokenDecimals)
```

```csharp
public static decimal ToDecimal(string amount, uint tokenDecimals)
```

```csharp
public static string ToDecimalString(string amount, uint tokenDecimals)
```

## PhantasmaPhoenix.Cryptography.IKeyPair

Source: `PhantasmaPhoenix.Cryptography/src/Abstractions/IKeyPair.cs`

### Declarations

```csharp
public interface IKeyPair
```

## PhantasmaPhoenix.Cryptography.Base16

Source: `PhantasmaPhoenix.Cryptography/src/Common/Base16.cs`

### Declarations

```csharp
public static class Base16
```

### Methods

```csharp
public static byte[]? Decode(this string input, bool allowExceptions = true)
```

```csharp
public static string Encode(this byte[] input)
```

## PhantasmaPhoenix.Cryptography.Base58

Source: `PhantasmaPhoenix.Cryptography/src/Common/Base58.cs`

### Declarations

```csharp
public static class Base58
```

### Methods

```csharp
public const string Alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz";
```

```csharp
public static byte[] Decode(string input)
```

```csharp
public static string Encode(byte[] input)
```

## PhantasmaPhoenix.Cryptography.ECDsaCurve

Source: `PhantasmaPhoenix.Cryptography/src/Cryptography/ECDsa/ECDsa.Curves.cs`

### Declarations

```csharp
public enum ECDsaCurve
```

### Variants

- `Secp256k1`
- `Secp256r1`

## PhantasmaPhoenix.Cryptography.ECDsaHelpers

Source: `PhantasmaPhoenix.Cryptography/src/Cryptography/ECDsa/ECDsa.Helpers.cs`

### Declarations

```csharp
public static class ECDsaHelpers
```

### Methods

```csharp
public static ECDomainParameters GetECDomainParameters(ECDsaCurve curve)
```

```csharp
public static ECPrivateKeyParameters GetECPrivateKeyParameters(ECDsaCurve curve, byte[] privateKey)
```

```csharp
public static ECPublicKeyParameters GetECPublicKeyParameters(ECDsaCurve curve, byte[] publicKey)
```

```csharp
public static X9ECParameters GetECParameters(ECDsaCurve curve)
```

```csharp
public static byte[] FromDER(byte[] derSignature, int outputLength = 64)
```

```csharp
public static byte[] ToDER(byte[] signature)
```

## PhantasmaPhoenix.Cryptography.ECDsaSignature

Source: `PhantasmaPhoenix.Cryptography/src/Cryptography/ECDsa/ECDsa.Signature.cs`

### Declarations

```csharp
public class ECDsaSignature : Signature
```

### Methods

```csharp
public ECDsaCurve Curve { get; private set; }
```

```csharp
public ECDsaSignature(byte[] bytes, ECDsaCurve curve)
```

```csharp
public byte[] Bytes { get; private set; }
```

```csharp
public override SignatureKind Kind => SignatureKind.ECDSA;
```

```csharp
public override bool Equals(object obj)
```

```csharp
public override bool Verify(byte[] message, IEnumerable<Address> addresses)
```

```csharp
public override int GetHashCode()
```

```csharp
public override void SerializeData(BinaryWriter writer)
```

```csharp
public override void UnserializeData(BinaryReader reader)
```

```csharp
public static ECDsaSignature Generate(IKeyPair keypair, byte[] message, ECDsaCurve curve, Func<byte[], byte[], byte[], byte[]>? customSignFunction = null)
```

```csharp
public static byte[] ExtractPublicKeyFromAddress(Address address)
```

## PhantasmaPhoenix.Cryptography.ECDsa

Source: `PhantasmaPhoenix.Cryptography/src/Cryptography/ECDsa/ECDsa.cs`

### Declarations

```csharp
public static class ECDsa
```

### Methods

```csharp
public static bool Verify(byte[] message, byte[] signature, byte[] pubkey, ECDsaCurve curve)
```

```csharp
public static byte[] CompressPublicKey(byte[] uncompressedPublicKey)
```

```csharp
public static byte[] DecompressPublicKey(byte[] compressedPublicKey, ECDsaCurve curve, bool dropUncompressedKeyPrefixByte = false)
```

```csharp
public static byte[] GetPublicKey(byte[] privateKey, bool compressed, ECDsaCurve curve)
```

```csharp
public static byte[] Sign(byte[] message, byte[] prikey, ECDsaCurve curve)
```

```csharp
public static byte[] SignDeterministic(byte[] message, byte[] prikey, ECDsaCurve curve)
```

## PhantasmaPhoenix.Cryptography.Ed25519Signature

Source: `PhantasmaPhoenix.Cryptography/src/Cryptography/EdDSA/Ed25519.Signature.cs`

### Declarations

```csharp
public class Ed25519Signature : Signature
```

### Methods

```csharp
public Ed25519Signature(byte[] bytes)
```

```csharp
public byte[] Bytes { get; private set; }
```

```csharp
public override SignatureKind Kind => SignatureKind.Ed25519;
```

```csharp
public override bool Equals(object obj)
```

```csharp
public override bool Verify(byte[] message, IEnumerable<Address> addresses)
```

```csharp
public override int GetHashCode()
```

```csharp
public override void SerializeData(BinaryWriter writer)
```

```csharp
public override void UnserializeData(BinaryReader reader)
```

```csharp
public static Ed25519Signature Generate(IKeyPair keypair, byte[] message)
```

## PhantasmaPhoenix.Cryptography.Ed25519

Source: `PhantasmaPhoenix.Cryptography/src/Cryptography/EdDSA/Ed25519.cs`

### Declarations

```csharp
public static class Ed25519
```

### Methods

```csharp
public const int ExpandedPrivateKeySizeInBytes = 32 * 2;
```

```csharp
public const int PrivateKeySeedSizeInBytes = 32;
```

```csharp
public const int PublicKeySizeInBytes = 32;
```

```csharp
public const int SharedKeySizeInBytes = 32;
```

```csharp
public const int SignatureSizeInBytes = 64;
```

```csharp
public static bool Verify(byte[] signature, byte[] message, byte[] publicKey)
```

```csharp
public static byte[] PublicKeyFromSeed(byte[] privateKey)
```

```csharp
public static byte[] Sign(byte[] message, byte[] expandedPrivateKey)
```

## PhantasmaPhoenix.Cryptography.Entropy

Source: `PhantasmaPhoenix.Cryptography/src/Cryptography/Entropy.cs`

### Declarations

```csharp
public static class Entropy
```

### Methods

```csharp
public static byte[] GetRandomBytes(int targetLength)
```

## PhantasmaPhoenix.Cryptography.Extensions.Base58Extensions

Source: `PhantasmaPhoenix.Cryptography/src/Cryptography/Extensions/Base58Extensions.cs`

### Declarations

```csharp
public static class Base58Extensions
```

### Methods

```csharp
public static byte[] Base58CheckDecode(this string input)
```

```csharp
public static string Base58CheckEncode(this byte[] data)
```

## PhantasmaPhoenix.Cryptography.Extensions.HashExtensions

Source: `PhantasmaPhoenix.Cryptography/src/Cryptography/Extensions/HashExtensions.cs`

### Declarations

```csharp
public static class HashExtensions
```

### Methods

```csharp
public static byte[] Blake2b_256(this byte[] value, int offset, int count)
```

```csharp
public static byte[] Sha256(this IEnumerable<byte> value)
```

```csharp
public static byte[] Sha256(this byte[] value, int offset, int count)
```

```csharp
public static byte[] Sha256(this string value)
```

## PhantasmaPhoenix.Cryptography.Hash

Source: `PhantasmaPhoenix.Cryptography/src/Cryptography/Hash/Hash.cs`

### Declarations

```csharp
public struct Hash : ISerializable, IComparable<Hash>, IEquatable<Hash>
```

### Methods

```csharp
public Hash(byte[] value)
```

```csharp
public bool IsNull
```

```csharp
public byte[] ToByteArray()
```

```csharp
public byte[] ToByteArrayReversed()
```

```csharp
public const int Length = 32;
```

```csharp
public int CompareTo(Hash other)
```

```csharp
public int Size => _data.Length;
```

```csharp
public override bool Equals(object? obj)
```

```csharp
public override int GetHashCode() => (int)_data.ToUInt32(0);
```

```csharp
public override string ToString()
```

```csharp
public static Hash FromBytes(byte[] input)
```

```csharp
public static Hash FromString(string str)
```

```csharp
public static Hash FromUnpaddedHex(string hash)
```

```csharp
public static Hash MerkleCombine(Hash A, Hash B)
```

```csharp
public static Hash Parse(string s)
```

```csharp
public static bool TryParse(string s, out Hash result)
```

```csharp
public static bool operator !=(Hash left, Hash right)
```

```csharp
public static bool operator <(Hash left, Hash right)
```

```csharp
public static bool operator <=(Hash left, Hash right)
```

```csharp
public static bool operator ==(Hash left, Hash right)
```

```csharp
public static bool operator >(Hash left, Hash right)
```

```csharp
public static bool operator >=(Hash left, Hash right)
```

```csharp
public static implicit operator BigInteger(Hash val)
```

```csharp
public static implicit operator Hash(BigInteger val)
```

```csharp
public static readonly Hash Null = FromBytes(new byte[Length]);
```

```csharp
public static readonly Hash Zero = new Hash();
```

```csharp
public void SerializeData(BinaryWriter writer)
```

```csharp
public void UnserializeData(BinaryReader reader)
```

## PhantasmaPhoenix.Cryptography.AddressKind

Source: `PhantasmaPhoenix.Cryptography/src/Enums.cs`

### Declarations

```csharp
public enum AddressKind
```

### Variants

- `Interop = 3`
- `Invalid = 0`
- `System = 2`
- `User = 1`

## PhantasmaPhoenix.Cryptography.SignatureKind

Source: `PhantasmaPhoenix.Cryptography/src/Enums.cs`

### Declarations

```csharp
public enum SignatureKind
```

### Variants

- `ECDSA`
- `Ed25519`
- `None`

## PhantasmaPhoenix.Cryptography.MnemonicPhraseLength

Source: `PhantasmaPhoenix.Cryptography/src/Mnemonics/Enums.cs`

### Declarations

```csharp
public enum MnemonicPhraseLength
```

### Variants

- `Twelve_Words`
- `Twenty_Four_Words`

## PhantasmaPhoenix.Cryptography.Mnemonics

Source: `PhantasmaPhoenix.Cryptography/src/Mnemonics/Mnemonics.cs`

### Declarations

```csharp
public static class Mnemonics
```

### Methods

```csharp
public static (byte[]?, string?) MnemonicToPK(string mnemonicPhrase, uint pkIndex = 0)
```

```csharp
public static (string?, string?) MnemonicToWif(string mnemonicPhrase, uint pkIndex = 0)
```

```csharp
public static string GenerateMnemonic(MnemonicPhraseLength mnemonicPhraseLength)
```

## PhantasmaPhoenix.Cryptography.Extensions.BinaryIoStructuresExtensions

Source: `PhantasmaPhoenix.Cryptography/src/Serialization/Extensions/BinaryIoStructuresExtensions.cs`

### Declarations

```csharp
public static class BinaryIoStructuresExtensions
```

### Methods

```csharp
public static Address ReadAddress(this BinaryReader reader)
```

```csharp
public static Hash ReadHash(this BinaryReader reader)
```

```csharp
public static Signature ReadSignature(this BinaryReader reader)
```

```csharp
public static byte[] ReadPublicKey(this BinaryReader reader)
```

```csharp
public static void WriteAddress(this BinaryWriter writer, Address address)
```

```csharp
public static void WriteHash(this BinaryWriter writer, Hash hash)
```

```csharp
public static void WritePublicKey(this BinaryWriter writer, byte[] publicKey)
```

```csharp
public static void WriteSignature(this BinaryWriter writer, Signature signature)
```

## PhantasmaPhoenix.Cryptography.Address

Source: `PhantasmaPhoenix.Cryptography/src/Structures/Address.cs`

### Declarations

```csharp
public struct Address : ISerializable, IComparable<Address>
```

### Methods

```csharp
public AddressKind Kind => IsNull ? AddressKind.System : (_bytes[0] >= 3) ? AddressKind.Interop : (AddressKind)_bytes[0];
```

```csharp
public bool IsInterop => Kind == AddressKind.Interop;
```

```csharp
public bool IsNull
```

```csharp
public bool IsSystem => Kind == AddressKind.System;
```

```csharp
public bool IsUser => Kind == AddressKind.User;
```

```csharp
public bool ValidateSignedData(string signedData, string random, string data)
```

```csharp
public byte PlatformID => (byte)(1 + _bytes[0] - AddressKind.Interop);
```

```csharp
public byte[] GetPublicKey()
```

```csharp
public byte[] ToByteArray()
```

```csharp
public const int LengthInBytes = 34;
```

```csharp
public const int MaxPlatformNameLength = 10;
```

```csharp
public int CompareTo(Address other)
```

```csharp
public int GetSize()
```

```csharp
public override bool Equals(object? obj)
```

```csharp
public override int GetHashCode()
```

```csharp
public override string ToString()
```

```csharp
public static Address EncodeAddress(byte platformID, string addressText)
```

```csharp
public static Address FromBytes(byte[] bytes)
```

```csharp
public static Address FromHash(byte[] input)
```

```csharp
public static Address FromHash(string str)
```

```csharp
public static Address FromInterop(byte platformID, byte[] publicKey)
```

```csharp
public static Address FromKey(IKeyPair key)
```

```csharp
public static Address Parse(string text, bool checkReservedByte = true)
```

```csharp
public static bool IsValidAddress(string text)
```

```csharp
public static bool operator !=(Address A, Address B)
```

```csharp
public static bool operator ==(Address A, Address B)
```

```csharp
public static readonly Address Null = new Address(NullPublicKey);
```

```csharp
public static readonly string NullText = "NULL";
```

```csharp
public string ConvertPhantasmaToEthereum()
```

```csharp
public string Text
```

```csharp
public void DecodeInterop(out byte platformID, out byte[] publicKey)
```

```csharp
public void SerializeData(BinaryWriter writer)
```

```csharp
public void UnserializeData(BinaryReader reader)
```

## PhantasmaPhoenix.Cryptography.PhantasmaKeys

Source: `PhantasmaPhoenix.Cryptography/src/Structures/KeyPair.cs`

### Declarations

```csharp
public sealed class PhantasmaKeys : IKeyPair
```

### Methods

```csharp
public PhantasmaKeys(byte[] privateKey)
```

```csharp
public Signature Sign(byte[] msg, Func<byte[], byte[], byte[], byte[]>? customSignFunction = null)
```

```csharp
public byte[] PrivateKey { get; private set; }
```

```csharp
public byte[] PublicKey { get; private set; }
```

```csharp
public const int PrivateKeyLength = 32;
```

```csharp
public override string ToString()
```

```csharp
public readonly Address Address;
```

```csharp
public static PhantasmaKeys FromWIF(string wif)
```

```csharp
public static PhantasmaKeys Generate()
```

```csharp
public string ToWIF()
```

## PhantasmaPhoenix.Cryptography.Signature

Source: `PhantasmaPhoenix.Cryptography/src/Structures/Signature.cs`

### Declarations

```csharp
public abstract class Signature : ISerializable
```

### Methods

```csharp
public abstract SignatureKind Kind { get; }
```

```csharp
public abstract bool Verify(byte[] message, IEnumerable<Address> addresses);
```

```csharp
public abstract void SerializeData(BinaryWriter writer);
```

```csharp
public abstract void UnserializeData(BinaryReader reader);
```

```csharp
public bool Verify(byte[] message, Address address)
```

```csharp
public byte[] ToByteArray()
```

```csharp
public override bool Equals(object? obj)
```

## PhantasmaPhoenix.Cryptography.Legacy.BIP39.BIP39

Source: `PhantasmaPhoenix.Cryptography.Legacy/src/Mnemonics/BIP39.cs`

### Declarations

```csharp
public class BIP39
```

### Methods

```csharp
public BIP39(string mnemonicSentence, string passphrase = cEmptyString)
```

```csharp
public byte[] SeedBytes
```

```csharp
public const string cEmptyString = "";
```

```csharp
public const string cSaltHeader = "mnemonic"; //this is the first part of the salt as described in the BIP39 spec
```

```csharp
public string MnemonicSentence
```

## PhantasmaPhoenix.Cryptography.Legacy.MnemonicsLegacy

Source: `PhantasmaPhoenix.Cryptography.Legacy/src/Mnemonics/MnemonicsLegacy.cs`

### Declarations

```csharp
public static class MnemonicsLegacy
```

### Methods

```csharp
public static string DecodeLegacySeedToWif(string mnemonicPhrase, string password)
```

## PhantasmaPhoenix.Cryptography.Legacy.PBKDF2.Rfc2898_pbkdf2_hmacsha512

Source: `PhantasmaPhoenix.Cryptography.Legacy/src/Mnemonics/RFC2898_PBDF2_HMAC-SHA512.cs`

### Declarations

```csharp
public class Rfc2898_pbkdf2_hmacsha512
```

### Methods

```csharp
public Byte[] GetDerivedKeyBytes_PBKDF2_HMACSHA512(Int32 keyLength)
```

```csharp
public Rfc2898_pbkdf2_hmacsha512(Byte[] password, Byte[] salt, int iterations = CMinIterations)
```

```csharp
public const int CMinIterations = 2048;
```

```csharp
public const int CMinSaltLength = 8;
```

```csharp
public const int hLen = 64;
```

```csharp
public static Byte[] PBKDF2(Byte[] P, Byte[] S, int c = CMinIterations, int dkLen = hLen)
```

## PhantasmaPhoenix.Cryptography.Legacy.Utilities

Source: `PhantasmaPhoenix.Cryptography.Legacy/src/Mnemonics/Utilities.cs`

### Declarations

```csharp
public static class Utilities
```

### Methods

```csharp
public static Byte[] MergeByteArrays(Byte[] source1, Byte[] source2)
```

```csharp
public static String NormaliseStringNfkd(String toNormalise)
```

```csharp
public static byte[] HmacSha512Digest(byte[] input, int offset, int length, byte[] hmacKey)
```

## PhantasmaPhoenix.Cryptography.Legacy.Storage.ArchiveEncryptionMode

Source: `PhantasmaPhoenix.Cryptography.Legacy/src/Storage/Abstractions/IArchiveEncryption.cs`

### Declarations

```csharp
public enum ArchiveEncryptionMode
```

### Variants

- `None`
- `Private`
- `Shared`

## PhantasmaPhoenix.Cryptography.Legacy.Storage.IArchiveEncryption

Source: `PhantasmaPhoenix.Cryptography.Legacy/src/Storage/Abstractions/IArchiveEncryption.cs`

### Declarations

```csharp
public interface IArchiveEncryption : ISerializable
```

## PhantasmaPhoenix.Cryptography.Legacy.Storage.ArchiveExtensions

Source: `PhantasmaPhoenix.Cryptography.Legacy/src/Storage/ArchiveExtensions.cs`

### Declarations

```csharp
public static class ArchiveExtensions
```

### Methods

```csharp
public static IArchiveEncryption ReadArchiveEncryption(byte[] bytes)
```

```csharp
public static IArchiveEncryption ReadArchiveEncryption(this BinaryReader reader)
```

```csharp
public static byte[] ToBytes(this IArchiveEncryption encryption)
```

```csharp
public static readonly byte[] Uncompressed = new byte[] { (byte)ArchiveEncryptionMode.None };
```

```csharp
public static void WriteArchiveEncryption(this BinaryWriter writer, IArchiveEncryption encryption)
```

## PhantasmaPhoenix.Cryptography.Legacy.Storage.AES

Source: `PhantasmaPhoenix.Cryptography.Legacy/src/Storage/Cryptography/AES.cs`

### Declarations

```csharp
public static class AES
```

### Methods

```csharp
public static byte[] GCMDecrypt(byte[] data, byte[] key, byte[] iv)
```

```csharp
public static byte[] GCMEncrypt(byte[] data, byte[] key, byte[] iv)
```

```csharp
public static byte[] GenerateIV(int vectorSize)
```

## PhantasmaPhoenix.Cryptography.Legacy.Storage.DiffieHellman

Source: `PhantasmaPhoenix.Cryptography.Legacy/src/Storage/Cryptography/DiffieHellman.cs`

### Declarations

```csharp
public static class DiffieHellman
```

### Methods

```csharp
public static byte[] Decrypt(byte[] input, byte[] key)
```

```csharp
public static byte[] Encrypt(byte[] input, byte[] key)
```

```csharp
public static byte[] GetSharedSecret(byte[] localPrivateKeyBytes, byte[] remotePublicKeyBytes)
```

## PhantasmaPhoenix.Cryptography.Legacy.Storage.PrivateArchiveEncryption

Source: `PhantasmaPhoenix.Cryptography.Legacy/src/Storage/PrivateArchiveEncryption.cs`

### Declarations

```csharp
public class PrivateArchiveEncryption : IArchiveEncryption
```

### Methods

```csharp
public Address Address { get; private set; }
```

```csharp
public ArchiveEncryptionMode Mode => ArchiveEncryptionMode.Private;
```

```csharp
public PrivateArchiveEncryption()
```

```csharp
public PrivateArchiveEncryption(Address publicKey)
```

```csharp
public byte[] ContentInitializationVector { get; private set; }
```

```csharp
public byte[] Decrypt(byte[] chunk, PhantasmaKeys keys)
```

```csharp
public byte[] Encrypt(byte[] chunk, PhantasmaKeys keys)
```

```csharp
public byte[] NameInitializationVector { get; private set; }
```

```csharp
public string DecryptName(string name, PhantasmaKeys keys)
```

```csharp
public string EncryptName(string name, PhantasmaKeys keys)
```

```csharp
public void SerializeData(BinaryWriter writer)
```

```csharp
public void UnserializeData(BinaryReader reader)
```

## PhantasmaPhoenix.Cryptography.Legacy.Storage.SharedArchiveEncryption

Source: `PhantasmaPhoenix.Cryptography.Legacy/src/Storage/SharedArchiveEncryption.cs`

### Declarations

```csharp
public class SharedArchiveEncryption : IArchiveEncryption
```

### Methods

```csharp
public Address Destination { get; private set; }
```

```csharp
public Address Source { get; private set; }
```

```csharp
public ArchiveEncryptionMode Mode => ArchiveEncryptionMode.Shared;
```

```csharp
public SharedArchiveEncryption()
```

```csharp
public byte[] Decrypt(byte[] chunk, PhantasmaKeys keys)
```

```csharp
public byte[] Encrypt(byte[] chunk, PhantasmaKeys keys)
```

```csharp
public string DecryptName(string name, PhantasmaKeys keys)
```

```csharp
public string EncryptName(string name, PhantasmaKeys keys)
```

```csharp
public void SerializeData(BinaryWriter writer)
```

```csharp
public void UnserializeData(BinaryReader reader)
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Signer.Crypto.ECDSASignature

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Crypto/ECDSASignature.cs`

### Declarations

```csharp
public class ECDSASignature
```

### Methods

```csharp
public BigInteger R { get; }
```

```csharp
public BigInteger S { get; }
```

```csharp
public ECDSASignature MakeCanonical()
```

```csharp
public ECDSASignature(BigInteger r, BigInteger s)
```

```csharp
public ECDSASignature(BigInteger[] rs)
```

```csharp
public ECDSASignature(byte[] derSig)
```

```csharp
public bool IsLowS => S.CompareTo(ECKey.HALF_CURVE_ORDER) <= 0;
```

```csharp
public byte[] ToDER()
```

```csharp
public byte[] V { get; set; }
```

```csharp
public static ECDSASignature FromDER(byte[] sig)
```

```csharp
public static bool IsValidDER(byte[] bytes)
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Signer.Crypto.ECKey

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Crypto/ECKey.cs`

### Declarations

```csharp
public class ECKey
```

### Methods

```csharp
public ECDomainParameters DomainParameter
```

```csharp
public ECKey(byte[] vch, bool isPrivate)
```

```csharp
public ECPrivateKeyParameters PrivateKey => _Key as ECPrivateKeyParameters;
```

```csharp
public ECPublicKeyParameters GetPublicKeyParameters()
```

```csharp
public bool Verify(byte[] hash, ECDSASignature sig)
```

```csharp
public byte[] GetPubKey(bool isCompressed)
```

```csharp
public static ECKey RecoverFromSignature(int recId, ECDSASignature sig, byte[] message, bool compressed)
```

```csharp
public static X9ECParameters Secp256k1 => _Secp256k1;
```

```csharp
public static readonly BigInteger CURVE_ORDER;
```

```csharp
public static readonly BigInteger HALF_CURVE_ORDER;
```

```csharp
public static readonly ECDomainParameters CURVE;
```

```csharp
public static readonly X9ECParameters _Secp256k1;
```

```csharp
public virtual ECDSASignature Sign(byte[] hash)
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Hex.HexConvertors.Extensions.HexBigIntegerConvertorExtensions

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Hex/Extensions/HexBigIntegerConvertorExtensions.cs`

### Declarations

```csharp
public static class HexBigIntegerConvertorExtensions
```

### Methods

```csharp
public static BigInteger HexToBigInteger(this string hex, bool isHexLittleEndian)
```

```csharp
public static byte[] ToByteArray(this BigInteger value, bool littleEndian)
```

```csharp
public static string ToHex(this BigInteger value, bool littleEndian, bool compact = true, bool add0x = true)
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Hex.HexConvertors.Extensions.HexByteConvertorExtensions

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Hex/Extensions/HexByteConvertorExtensions.cs`

### Declarations

```csharp
public static class HexByteConvertorExtensions
```

### Methods

```csharp
public static bool HasHexPrefix(this string value)
```

```csharp
public static bool IsHex(this string value)
```

```csharp
public static bool IsTheSameHex(this string first, string second)
```

```csharp
public static byte[] HexToByteArray(this string value)
```

```csharp
public static string EnsureHexPrefix(this string value)
```

```csharp
public static string RemoveHexPrefix(this string value)
```

```csharp
public static string ToHex(this byte[] value, bool prefix = false)
```

```csharp
public static string ToHexCompact(this byte[] value)
```

```csharp
public static string[] EnsureHexPrefix(this string[] values)
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.EthereumKey

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/KeyPair.cs`

### Declarations

```csharp
public class EthereumKey : IKeyPair
```

### Methods

```csharp
public EthereumKey(byte[] privateKey)
```

```csharp
public Signature Sign(byte[] msg, Func<byte[], byte[], byte[], byte[]> customSignFunction = null)
```

```csharp
public byte[] PrivateKey { get; private set; }
```

```csharp
public byte[] PublicKey { get; private set; }
```

```csharp
public override string ToString()
```

```csharp
public readonly byte[] CompressedPublicKey;
```

```csharp
public readonly byte[] UncompressedPublicKey;
```

```csharp
public readonly string Address;
```

```csharp
public static EthereumKey FromPrivateKey(string prv)
```

```csharp
public static EthereumKey FromWIF(string wif)
```

```csharp
public static EthereumKey Generate()
```

```csharp
public static byte[] FromWIFToBytes(string wif)
```

```csharp
public static string PublicKeyToAddress(byte[] publicKey, ECDsaCurve curve)
```

```csharp
public string GetWIF()
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Model.DefaultValues

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Model/DefaultValues.cs`

### Declarations

```csharp
public class DefaultValues
```

### Methods

```csharp
public static DefaultValues Current { get; } = new DefaultValues();
```

```csharp
public static byte[] EMPTY_BYTE_ARRAY = new byte[0];
```

```csharp
public static readonly byte[] EMPTY_DATA_HASH = Sha3Keccack.Current.CalculateHash(EMPTY_BYTE_ARRAY);
```

```csharp
public static readonly byte[] EMPTY_TRIE_HASH = Sha3Keccack.Current.CalculateHash(RLP.RLP.EncodeElement(EMPTY_BYTE_ARRAY));
```

```csharp
public static readonly byte[] ZERO_BYTE_ARRAY = { 0 };
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.RLP.ConvertorForRLPEncodingExtensions

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/RLP/ConvertorForRLPEncodingExtensions.cs`

### Declarations

```csharp
public static class ConvertorForRLPEncodingExtensions
```

### Methods

```csharp
public static BigInteger ToBigIntegerFromRLPDecoded(this byte[] bytes)
```

```csharp
public static byte[] ToBytesForRLPEncoding(this BigInteger bigInteger)
```

```csharp
public static byte[] ToBytesForRLPEncoding(this int number)
```

```csharp
public static byte[] ToBytesForRLPEncoding(this long number)
```

```csharp
public static byte[] ToBytesForRLPEncoding(this string str)
```

```csharp
public static byte[][] ToBytesForRLPEncoding(this string[] strings)
```

```csharp
public static int ToIntFromRLPDecoded(this byte[] bytes)
```

```csharp
public static long ToLongFromRLPDecoded(this byte[] bytes)
```

```csharp
public static string ToStringFromRLPDecoded(this byte[] bytes)
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.RLP.IRLPElement

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/RLP/IRLPElement.cs`

### Declarations

```csharp
public interface IRLPElement
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.RLP.RLP

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/RLP/RLP.cs`

### Declarations

```csharp
public class RLP
```

### Methods

```csharp
public static IRLPElement Decode(byte[] msgData)
```

```csharp
public static IRLPElement DecodeFirstElement(byte[] msgData, int startPos)
```

```csharp
public static bool IsNullOrZeroArray(byte[] array)
```

```csharp
public static bool IsSingleZero(byte[] array)
```

```csharp
public static byte[] EncodeByte(byte singleByte)
```

```csharp
public static byte[] EncodeElement(byte[] srcData)
```

```csharp
public static byte[] EncodeElementsAndList(params byte[][] dataItems)
```

```csharp
public static byte[] EncodeList(params byte[][] items)
```

```csharp
public static int ByteArrayToInt(byte[] bytes)
```

```csharp
public static readonly byte[] EMPTY_BYTE_ARRAY = new byte[0];
```

```csharp
public static readonly byte[] ZERO_BYTE_ARRAY = { 0 };
```

```csharp
public static void Decode(byte[] msgData, int level, int startPosition, int endPosition, int levelToIndex, RLPCollection rlpCollection)
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.RLP.RLPCollection

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/RLP/RLPCollection.cs`

### Declarations

```csharp
public class RLPCollection : List<IRLPElement>, IRLPElement
```

### Methods

```csharp
public byte[] RLPData { get; set; }
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.RLP.RLPItem

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/RLP/RLPItem.cs`

### Declarations

```csharp
public class RLPItem : IRLPElement
```

### Methods

```csharp
public RLPItem(byte[] rlpData)
```

```csharp
public byte[] RLPData => GetRLPData();
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Signer.ECDSASignatureFactory

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Signer/ECDSASignatureFactory.cs`

### Declarations

```csharp
public class ECDSASignatureFactory
```

### Methods

```csharp
public static ECDSASignature ExtractECDSASignature(byte[] signatureArray)
```

```csharp
public static ECDSASignature ExtractECDSASignature(string signature)
```

```csharp
public static ECDSASignature FromComponents(byte[] r, byte[] s)
```

```csharp
public static ECDSASignature FromComponents(byte[] r, byte[] s, byte v)
```

```csharp
public static ECDSASignature FromComponents(byte[] r, byte[] s, byte[] v)
```

```csharp
public static ECDSASignature FromComponents(byte[] rs)
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Signer.EthECDSASignature

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Signer/EthECDSASignature.cs`

### Declarations

```csharp
public class EthECDSASignature
```

### Methods

```csharp
public EthECDSASignature(BigInteger r, BigInteger s, byte[] v)
```

```csharp
public EthECDSASignature(byte[] derSig)
```

```csharp
public bool IsLowS => ECDSASignature.IsLowS;
```

```csharp
public bool IsVSignedForChain()
```

```csharp
public byte[] R => ECDSASignature.R.ToByteArrayUnsigned();
```

```csharp
public byte[] S => ECDSASignature.S.ToByteArrayUnsigned();
```

```csharp
public byte[] To64ByteArray()
```

```csharp
public byte[] ToDER()
```

```csharp
public byte[] V
```

```csharp
public static EthECDSASignature FromDER(byte[] sig)
```

```csharp
public static bool IsValidDER(byte[] bytes)
```

```csharp
public static string CreateStringSignature(EthECDSASignature signature)
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Signer.EthECDSASignatureFactory

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Signer/EthECDSASignatureFactory.cs`

### Declarations

```csharp
public class EthECDSASignatureFactory
```

### Methods

```csharp
public static EthECDSASignature ExtractECDSASignature(string signature)
```

```csharp
public static EthECDSASignature FromComponents(byte[] r, byte[] s)
```

```csharp
public static EthECDSASignature FromComponents(byte[] r, byte[] s, byte v)
```

```csharp
public static EthECDSASignature FromComponents(byte[] r, byte[] s, byte[] v)
```

```csharp
public static EthECDSASignature FromComponents(byte[] rs)
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Signer.EthECKey

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Signer/EthECKey.cs`

### Declarations

```csharp
public class EthECKey
```

### Methods

```csharp
public EthECDSASignature Sign(byte[] hash)
```

```csharp
public EthECDSASignature SignAndCalculateV(byte[] hash)
```

```csharp
public EthECDSASignature SignAndCalculateV(byte[] hash, BigInteger chainId)
```

```csharp
public EthECKey(byte[] vch, bool isPrivate)
```

```csharp
public EthECKey(byte[] vch, bool isPrivate, byte prefix)
```

```csharp
public EthECKey(string privateKey)
```

```csharp
public bool Verify(byte[] hash, EthECDSASignature sig)
```

```csharp
public bool VerifyAllowingOnlyLowS(byte[] hash, EthECDSASignature sig)
```

```csharp
public byte[] CalculateCommonSecret(EthECKey publicKey)
```

```csharp
public byte[] GetPrivateKeyAsBytes()
```

```csharp
public byte[] GetPubKey()
```

```csharp
public byte[] GetPubKeyNoPrefix()
```

```csharp
public static BigInteger GetChainFromVChain(BigInteger vChain)
```

```csharp
public static EthECKey GenerateKey()
```

```csharp
public static EthECKey RecoverFromSignature(EthECDSASignature signature, byte[] hash)
```

```csharp
public static EthECKey RecoverFromSignature(EthECDSASignature signature, byte[] hash, BigInteger chainId)
```

```csharp
public static EthECKey RecoverFromSignature(EthECDSASignature signature, int recId, byte[] hash)
```

```csharp
public static byte DEFAULT_PREFIX = 0x04;
```

```csharp
public static int GetRecIdFromV(byte v)
```

```csharp
public static int GetRecIdFromV(byte[] v)
```

```csharp
public static int GetRecIdFromVChain(BigInteger vChain, BigInteger chainId)
```

```csharp
public static int GetRecIdFromVChain(byte[] vChain, BigInteger chainId)
```

```csharp
public static string GetPublicAddress(string privateKey)
```

```csharp
public string GetPrivateKey()
```

```csharp
public string GetPublicAddress()
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Signer.ExternalSignerTransactionFormat

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Signer/IEthExternalSigner.cs`

### Declarations

```csharp
public enum ExternalSignerTransactionFormat
```

### Variants

- `Hash`
- `RLP`
- `Transaction`

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Signer.IEthExternalSigner

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Signer/IEthExternalSignerBase.cs`

### Declarations

```csharp
public interface IEthExternalSigner
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Signer.RLPDecoder

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Signer/RLPDecoder.cs`

### Declarations

```csharp
public class RLPDecoder
```

### Methods

```csharp
public static SignedData DecodeSigned(byte[] rawdata, int numberOfEncodingElements)
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Signer.RLPEncoder

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Signer/RLPEncoder.cs`

### Declarations

```csharp
public class RLPEncoder
```

### Methods

```csharp
public static byte[] EncodeSigned(SignedData signedData, int numberOfElements)
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Signer.RLPSigner

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Signer/RLPSigner.cs`

### Declarations

```csharp
public class RLPSigner
```

### Methods

```csharp
public EthECDSASignature Signature { get; private set; }
```

```csharp
public RLPSigner(byte[] rawData, int numberOfEncodingElements)
```

```csharp
public RLPSigner(byte[][] data) : this(data, data.Length)
```

```csharp
public RLPSigner(byte[][] data, byte[] r, byte[] s, byte v) : this(data, r, s, v, data.Length)
```

```csharp
public RLPSigner(byte[][] data, byte[] r, byte[] s, byte v, int numberOfEncodingElements)
```

```csharp
public RLPSigner(byte[][] data, byte[] r, byte[] s, byte[] v) : this(data, r, s, v, data.Length)
```

```csharp
public RLPSigner(byte[][] data, byte[] r, byte[] s, byte[] v, int numberOfEncodingElements)
```

```csharp
public RLPSigner(byte[][] data, int numberOfEncodingElements)
```

```csharp
public bool IsVSignatureForChain()
```

```csharp
public byte[] GetRLPEncoded()
```

```csharp
public byte[] GetRLPEncodedRaw()
```

```csharp
public byte[] Hash
```

```csharp
public byte[] RawHash
```

```csharp
public byte[][] Data { get; private set; }
```

```csharp
public void AppendData(params byte[][] extraData)
```

```csharp
public void SetSignature(EthECDSASignature signature)
```

```csharp
public void Sign(EthECKey key)
```

```csharp
public void Sign(EthECKey key, BigInteger chainId)
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Signer.SignedData

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Signer/SignedData.cs`

### Declarations

```csharp
public class SignedData
```

### Methods

```csharp
public EthECDSASignature GetSignature()
```

```csharp
public SignedData()
```

```csharp
public SignedData(byte[][] data, EthECDSASignature signature)
```

```csharp
public bool IsSigned()
```

```csharp
public byte[] R { get; set; }
```

```csharp
public byte[] S { get; set; }
```

```csharp
public byte[] V { get; set; }
```

```csharp
public byte[][] Data { get; set; }
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Signer.SignedTransactionBase

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Signer/SignedTransactionBase.cs`

### Declarations

```csharp
public abstract class SignedTransactionBase
```

### Methods

```csharp
public EthECDSASignature Signature => SimpleRlpSigner.Signature;
```

```csharp
public abstract EthECKey Key { get; }
```

```csharp
public abstract Task SignExternallyAsync(IEthExternalSigner externalSigner);
```

```csharp
public byte[] Data => SimpleRlpSigner.Data[5];
```

```csharp
public byte[] GasLimit => SimpleRlpSigner.Data[2];
```

```csharp
public byte[] GasPrice => SimpleRlpSigner.Data[1] ?? DefaultValues.ZERO_BYTE_ARRAY;
```

```csharp
public byte[] GetRLPEncoded()
```

```csharp
public byte[] GetRLPEncodedRaw()
```

```csharp
public byte[] Nonce => SimpleRlpSigner.Data[0] ?? DefaultValues.ZERO_BYTE_ARRAY;
```

```csharp
public byte[] RawHash => SimpleRlpSigner.RawHash;
```

```csharp
public byte[] ReceiveAddress => SimpleRlpSigner.Data[3];
```

```csharp
public byte[] Value => SimpleRlpSigner.Data[4] ?? DefaultValues.ZERO_BYTE_ARRAY;
```

```csharp
public const int NUMBER_ENCODING_ELEMENTS = 6;
```

```csharp
public static RLPSigner CreateDefaultRLPSigner(byte[] rawData)
```

```csharp
public static readonly BigInteger DEFAULT_GAS_LIMIT = BigInteger.Parse("21000");
```

```csharp
public static readonly BigInteger DEFAULT_GAS_PRICE = BigInteger.Parse("20000000000");
```

```csharp
public virtual void Sign(EthECKey key)
```

```csharp
public void SetSignature(EthECDSASignature signature)
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Signer.Transaction

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Signer/Transaction.cs`

### Declarations

```csharp
public class Transaction : SignedTransactionBase
```

### Methods

```csharp
public Transaction(RLPSigner rlpSigner)
```

```csharp
public Transaction(byte[] nonce, byte[] gasPrice, byte[] gasLimit, byte[] receiveAddress, byte[] value, byte[] data)
```

```csharp
public Transaction(byte[] nonce, byte[] gasPrice, byte[] gasLimit, byte[] receiveAddress, byte[] value, byte[] data, byte[] r, byte[] s, byte v)
```

```csharp
public Transaction(byte[] rawData)
```

```csharp
public Transaction(string to, BigInteger amount, BigInteger nonce) : this(to, amount, nonce, DEFAULT_GAS_PRICE, DEFAULT_GAS_LIMIT)
```

```csharp
public Transaction(string to, BigInteger amount, BigInteger nonce, BigInteger gasPrice, BigInteger gasLimit) : this(to, amount, nonce, gasPrice, gasLimit, "")
```

```csharp
public Transaction(string to, BigInteger amount, BigInteger nonce, BigInteger gasPrice, BigInteger gasLimit, string data) : this(nonce.ToBytesForRLPEncoding(), gasPrice.ToBytesForRLPEncoding(), gasLimit.ToBytesForRLPEncoding(), to.HexToByteArray(), amount.ToBytesForRLPEncoding(), data.HexToByteArray() )
```

```csharp
public Transaction(string to, BigInteger amount, BigInteger nonce, string data) : this(to, amount, nonce, DEFAULT_GAS_PRICE, DEFAULT_GAS_LIMIT, data)
```

```csharp
public override EthECKey Key => EthECKey.RecoverFromSignature(SimpleRlpSigner.Signature, SimpleRlpSigner.RawHash);
```

```csharp
public override async Task SignExternallyAsync(IEthExternalSigner externalSigner)
```

```csharp
public string ToJsonHex()
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Signer.TransactionChainId

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Signer/TransactionChainId.cs`

### Declarations

```csharp
public class TransactionChainId : SignedTransactionBase
```

### Methods

```csharp
public BigInteger GetChainIdAsBigInteger()
```

```csharp
public TransactionChainId(RLPSigner rlpSigner)
```

```csharp
public TransactionChainId(byte[] nonce, byte[] gasPrice, byte[] gasLimit, byte[] receiveAddress, byte[] value, byte[] data, byte[] chainId)
```

```csharp
public TransactionChainId(byte[] nonce, byte[] gasPrice, byte[] gasLimit, byte[] receiveAddress, byte[] value, byte[] data, byte[] chainId, byte[] r, byte[] s, byte[] v)
```

```csharp
public TransactionChainId(byte[] rawData)
```

```csharp
public TransactionChainId(byte[] rawData, BigInteger chainId)
```

```csharp
public TransactionChainId(string to, BigInteger amount, BigInteger nonce, BigInteger chainId) : this(to, amount, nonce, DEFAULT_GAS_PRICE, DEFAULT_GAS_LIMIT, chainId)
```

```csharp
public TransactionChainId(string to, BigInteger amount, BigInteger nonce, BigInteger gasPrice, BigInteger gasLimit, BigInteger chainId) : this(to, amount, nonce, gasPrice, gasLimit, "", chainId)
```

```csharp
public TransactionChainId(string to, BigInteger amount, BigInteger nonce, BigInteger gasPrice, BigInteger gasLimit, string data, BigInteger chainId) : this(nonce.ToBytesForRLPEncoding(), gasPrice.ToBytesForRLPEncoding(), gasLimit.ToBytesForRLPEncoding(), to.HexToByteArray(), amount.ToBytesForRLPEncoding(), data.HexToByteArray(), chainId.ToBytesForRLPEncoding() )
```

```csharp
public TransactionChainId(string to, BigInteger amount, BigInteger nonce, string data, BigInteger chainId) : this(to, amount, nonce, DEFAULT_GAS_PRICE, DEFAULT_GAS_LIMIT, data, chainId)
```

```csharp
public byte[] ChainId => SimpleRlpSigner.Data[6];
```

```csharp
public byte[] RHash => SimpleRlpSigner.Data[7];
```

```csharp
public byte[] SHash => SimpleRlpSigner.Data[8];
```

```csharp
public override EthECKey Key => EthECKey.RecoverFromSignature(SimpleRlpSigner.Signature, SimpleRlpSigner.RawHash, ChainId.ToBigIntegerFromRLPDecoded());
```

```csharp
public override async Task SignExternallyAsync(IEthExternalSigner externalSigner)
```

```csharp
public override void Sign(EthECKey key)
```

```csharp
public string ToJsonHex()
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Util.AddressExtensions

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Util/AddressExtensions.cs`

### Declarations

```csharp
public static class AddressExtensions
```

### Methods

```csharp
public static bool IsAnEmptyAddress(this string address)
```

```csharp
public static bool IsEmptyOrEqualsAddress(this string address1, string candidate)
```

```csharp
public static bool IsEthereumChecksumAddress(this string address)
```

```csharp
public static bool IsNotAnEmptyAddress(this string address)
```

```csharp
public static bool IsTheSameAddress(this string address, string otherAddress)
```

```csharp
public static bool IsValidEthereumAddressHexFormat(this string address)
```

```csharp
public static bool IsValidEthereumAddressLength(this string address)
```

```csharp
public static string AddressValueOrEmpty(this string address)
```

```csharp
public static string ConvertToEthereumChecksumAddress(this string address)
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Util.UniqueAddressList

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Util/AddressUtil.cs`

### Declarations

```csharp
public class UniqueAddressList : HashSet<string>
```

### Methods

```csharp
public UniqueAddressList() : base(new AddressEqualityComparer()) { }
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Util.AddressEqualityComparer

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Util/AddressUtil.cs`

### Declarations

```csharp
public class AddressEqualityComparer : IEqualityComparer<string>
```

### Methods

```csharp
public bool Equals(string x, string y)
```

```csharp
public int GetHashCode(string obj)
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Util.AddressUtil

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Util/AddressUtil.cs`

### Declarations

```csharp
public class AddressUtil
```

### Methods

```csharp
public bool AreAddressesTheSame(string address1, string address2)
```

```csharp
public bool IsAnEmptyAddress(string address)
```

```csharp
public bool IsChecksumAddress(string address)
```

```csharp
public bool IsEmptyOrEqualsAddress(string address1, string candidate)
```

```csharp
public bool IsNotAnEmptyAddress(string address)
```

```csharp
public bool IsValidAddressLength(string address)
```

```csharp
public bool IsValidEthereumAddressHexFormat(string address)
```

```csharp
public const string AddressEmptyAsHex = "0x0";
```

```csharp
public static AddressUtil Current
```

```csharp
public string AddressValueOrEmpty(string address)
```

```csharp
public string ConvertToChecksumAddress(string address)
```

```csharp
public string ConvertToValid20ByteAddress(string address)
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Util.ByteUtil

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Util/ByteUtil.cs`

### Declarations

```csharp
public static class ByteUtil
```

### Methods

```csharp
public static IEnumerable<byte> MergeToEnum(params byte[][] arrays)
```

```csharp
public static byte[] AppendByte(byte[] bytes, byte b)
```

```csharp
public static byte[] InitialiseEmptyByteArray(int length)
```

```csharp
public static byte[] Merge(params byte[][] arrays)
```

```csharp
public static byte[] Slice(this byte[] org, int start, int end = int.MaxValue)
```

```csharp
public static byte[] XOR(this byte[] a, byte[] b)
```

```csharp
public static readonly byte[] EMPTY_BYTE_ARRAY = new byte[0];
```

```csharp
public static readonly byte[] ZERO_BYTE_ARRAY = { 0 };
```

## PhantasmaPhoenix.InteropChains.Legacy.Ethereum.Util.Sha3Keccack

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Ethereum/Util/Sha3Keccack.cs`

### Declarations

```csharp
public class Sha3Keccack
```

### Methods

```csharp
public byte[] CalculateHash(byte[] value)
```

```csharp
public static Sha3Keccack Current { get; } = new Sha3Keccack();
```

```csharp
public string CalculateHash(string value)
```

```csharp
public string CalculateHashFromHex(params string[] hexValues)
```

## PhantasmaPhoenix.InteropChains.Legacy.Neo2.NeoKeys

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Neo2/Core/NeoKeys.cs`

### Declarations

```csharp
public class NeoKeys
```

### Methods

```csharp
public NeoKeys(byte[] privateKey)
```

```csharp
public override string ToString()
```

```csharp
public readonly UInt160 PublicKeyHash;
```

```csharp
public readonly UInt160 signatureHashN2;
```

```csharp
public readonly UInt160 signatureHashN3;
```

```csharp
public readonly byte[] CompressedPublicKey;
```

```csharp
public readonly byte[] PrivateKey;
```

```csharp
public readonly byte[] PublicKey;
```

```csharp
public readonly byte[] signatureScriptN2;
```

```csharp
public readonly byte[] signatureScriptN3;
```

```csharp
public readonly string Address;
```

```csharp
public readonly string AddressN3;
```

```csharp
public readonly string WIF;
```

```csharp
public static NeoKeys FromWIF(string wif)
```

```csharp
public static byte[] CreateSignatureScript(byte[] bytes)
```

```csharp
public static byte[] CreateSignatureScriptN3(byte[] bytes)
```

```csharp
public static byte[] EncodePoint(byte[] bytes)
```

```csharp
public static string PublicKeyToN2Address(byte[] publicKey)
```

## PhantasmaPhoenix.InteropChains.Legacy.Neo2.OpCode

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Neo2/Core/Opcodes.cs`

### Declarations

```csharp
public enum OpCode : byte
```

### Variants

- `ABS = 0x90, // The input is made positive.`
- `ADD = 0x93, // a is added to b.`
- `AND = 0x84, // Boolean and between each bit in the inputs.`
- `APPCALL = 0x67`
- `APPEND = 0xC8`
- `ARRAYSIZE = 0xC0`
- `BOOLAND = 0x9A, // If both a and b are not 0, the output is 1. Otherwise 0.`
- `BOOLOR = 0x9B, // If a or b is not 0, the output is 1. Otherwise 0.`
- `CALL = 0x65`
- `CALL_E = 0xE1`
- `CALL_ED = 0xE2`
- `CALL_EDT = 0xE4`
- `CALL_ET = 0xE3`
- `CALL_I = 0xE0`
- `CAT = 0x7E, // Concatenates two strings.`
- `CHECKMULTISIG = 0xAE`
- `CHECKSIG = 0xAC`
- `DEC = 0x8C, // 1 is subtracted from the input.`
- `DEPTH = 0x74, // Puts the number of stack items onto the stack.`
- `DIV = 0x96, // a is divided by b.`
- `DROP = 0x75, // Removes the top stack item.`
- `DUP = 0x76, // Duplicates the top stack item.`
- `DUPFROMALTSTACK = 0x6A`
- `EQUAL = 0x87, // Returns 1 if the inputs are exactly equal, 0 otherwise.`
- `FROMALTSTACK = 0x6C, // Puts the input onto the top of the main stack. Removes it from the alt stack.`
- `GT = 0xA0, // Returns 1 if a is greater than b, 0 otherwise.`
- `GTE = 0xA2, // Returns 1 if a is greater than or equal to b, 0 otherwise.`
- `HASH160 = 0xA9`
- `HASH256 = 0xAA`
- `HASKEY = 0xCB`
- `INC = 0x8B, // 1 is added to the input.`
- `INVERT = 0x83, // Flips all of the bits in the input.`
- `JMP = 0x62`
- `JMPIF = 0x63`
- `JMPIFNOT = 0x64`
- `KEYS = 0xCC`
- `LEFT = 0x80, // Keeps only characters left of the specified point in a string.`
- `LT = 0x9F, // Returns 1 if a is less than b, 0 otherwise.`
- `LTE = 0xA1, // Returns 1 if a is less than or equal to b, 0 otherwise.`
- `MAX = 0xA4, // Returns the larger of a and b.`
- `MIN = 0xA3, // Returns the smaller of a and b.`
- `MOD = 0x97, // Returns the remainder after dividing a by b.`
- `MUL = 0x95, // a is multiplied by b.`
- `NEGATE = 0x8F, // The sign of the input is flipped.`
- `NEWARRAY = 0xC5, //用作引用類型`
- `NEWMAP = 0xC7`
- `NEWSTRUCT = 0xC6, //用作值類型`
- `NIP = 0x77, // Removes the second-to-top stack item.`
- `NOP = 0x61, // Does nothing.`
- `NOT = 0x91, // If the input is 0 or 1, it is flipped. Otherwise the output will be 0.`
- `NUMEQUAL = 0x9C, // Returns 1 if the numbers are equal, 0 otherwise.`
- `NUMNOTEQUAL = 0x9E, // Returns 1 if the numbers are not equal, 0 otherwise.`
- `NZ = 0x92, // Returns 0 if the input is 0. 1 otherwise.`
- `OR = 0x85, // Boolean or between each bit in the inputs.`
- `OVER = 0x78, // Copies the second-to-top stack item to the top.`
- `PACK = 0xC1`
- `PICK = 0x79, // The item n back in the stack is copied to the top.`
- `PICKITEM = 0xC3`
- `PUSH0 = 0x00, // An empty array of bytes is pushed onto the stack.`
- `PUSH1 = 0x51, // The number 1 is pushed onto the stack.`
- `PUSH10 = 0x5A, // The number 10 is pushed onto the stack.`
- `PUSH11 = 0x5B, // The number 11 is pushed onto the stack.`
- `PUSH12 = 0x5C, // The number 12 is pushed onto the stack.`
- `PUSH13 = 0x5D, // The number 13 is pushed onto the stack.`
- `PUSH14 = 0x5E, // The number 14 is pushed onto the stack.`
- `PUSH15 = 0x5F, // The number 15 is pushed onto the stack.`
- `PUSH16 = 0x60, // The number 16 is pushed onto the stack.`
- `PUSH2 = 0x52, // The number 2 is pushed onto the stack.`
- `PUSH3 = 0x53, // The number 3 is pushed onto the stack.`
- `PUSH4 = 0x54, // The number 4 is pushed onto the stack.`
- `PUSH5 = 0x55, // The number 5 is pushed onto the stack.`
- `PUSH6 = 0x56, // The number 6 is pushed onto the stack.`
- `PUSH7 = 0x57, // The number 7 is pushed onto the stack.`
- `PUSH8 = 0x58, // The number 8 is pushed onto the stack.`
- `PUSH9 = 0x59, // The number 9 is pushed onto the stack.`
- `PUSHBYTES1 = 0x01, // 0x01-0x4B The next opcode bytes is data to be pushed onto the stack`
- `PUSHBYTES10 = 0xA`
- `PUSHBYTES11 = 0xB`
- `PUSHBYTES12 = 0xC`
- `PUSHBYTES13 = 0xD`
- `PUSHBYTES14 = 0xE`
- `PUSHBYTES15 = 0xF`
- `PUSHBYTES16 = 0x10`
- `PUSHBYTES17 = 0x11`
- `PUSHBYTES18 = 0x12`
- `PUSHBYTES19 = 0x13`
- `PUSHBYTES2 = 0x2`
- `PUSHBYTES20 = 0x14`
- `PUSHBYTES21 = 0x15`
- `PUSHBYTES22 = 0x16`
- `PUSHBYTES23 = 0x17`
- `PUSHBYTES24 = 0x18`
- `PUSHBYTES25 = 0x19`
- `PUSHBYTES26 = 0x1A`
- `PUSHBYTES27 = 0x1B`
- `PUSHBYTES28 = 0x1C`
- `PUSHBYTES29 = 0x1D`
- `PUSHBYTES3 = 0x3`
- `PUSHBYTES30 = 0x1E`
- `PUSHBYTES31 = 0x1F`
- `PUSHBYTES32 = 0x20`
- `PUSHBYTES33 = 0x21`
- `PUSHBYTES34 = 0x22`
- `PUSHBYTES35 = 0x23`
- `PUSHBYTES36 = 0x24`
- `PUSHBYTES37 = 0x25`
- `PUSHBYTES38 = 0x26`
- `PUSHBYTES39 = 0x27`
- `PUSHBYTES4 = 0x4`
- `PUSHBYTES40 = 0x28`
- `PUSHBYTES41 = 0x29`
- `PUSHBYTES42 = 0x2A`
- `PUSHBYTES43 = 0x2B`
- `PUSHBYTES44 = 0x2C`
- `PUSHBYTES45 = 0x2D`
- `PUSHBYTES46 = 0x2E`
- `PUSHBYTES47 = 0x2F`
- `PUSHBYTES48 = 0x30`
- `PUSHBYTES49 = 0x31`
- `PUSHBYTES5 = 0x5`
- `PUSHBYTES50 = 0x32`
- `PUSHBYTES51 = 0x33`
- `PUSHBYTES52 = 0x34`
- `PUSHBYTES53 = 0x35`
- `PUSHBYTES54 = 0x36`
- `PUSHBYTES55 = 0x37`
- `PUSHBYTES56 = 0x38`
- `PUSHBYTES57 = 0x39`
- `PUSHBYTES58 = 0x3A`
- `PUSHBYTES59 = 0x3B`
- `PUSHBYTES6 = 0x6`
- `PUSHBYTES60 = 0x3C`
- `PUSHBYTES61 = 0x3D`
- `PUSHBYTES62 = 0x3E`
- `PUSHBYTES63 = 0x3F`
- `PUSHBYTES64 = 0x40`
- `PUSHBYTES65 = 0x41`
- `PUSHBYTES66 = 0x42`
- `PUSHBYTES67 = 0x43`
- `PUSHBYTES68 = 0x44`
- `PUSHBYTES69 = 0x45`
- `PUSHBYTES7 = 0x7`
- `PUSHBYTES70 = 0x46`
- `PUSHBYTES71 = 0x47`
- `PUSHBYTES72 = 0x48`
- `PUSHBYTES73 = 0x49`
- `PUSHBYTES74 = 0x4A`
- `PUSHBYTES75 = 0x4B`
- `PUSHBYTES8 = 0x8`
- `PUSHBYTES9 = 0x9`
- `PUSHDATA1 = 0x0C, // The next byte contains the number of bytes to be pushed onto the stack.`
- `PUSHDATA2 = 0x0D, // The next two bytes contain the number of bytes to be pushed onto the stack.`
- `PUSHDATA4 = 0x0E, // The next four bytes contain the number of bytes to be pushed onto the stack.`
- `PUSHF = PUSH0`
- `PUSHM1 = 0x4F, // The number -1 is pushed onto the stack.`
- `PUSHT = PUSH1`
- `REMOVE = 0xCA`
- `RET = 0x66`
- `REVERSE = 0xC9`
- `RIGHT = 0x81, // Keeps only characters right of the specified point in a string.`
- `ROLL = 0x7A, // The item n back in the stack is moved to the top.`
- `ROT = 0x7B, // The top three items on the stack are rotated to the left.`
- `SETITEM = 0xC4`
- `SHA1 = 0xA7, // The input is hashed using SHA-1.`
- `SHA256 = 0xA8, // The input is hashed using SHA-256.`
- `SHL = 0x98, // Shifts a left b bits, preserving sign.`
- `SHR = 0x99, // Shifts a right b bits, preserving sign.`
- `SIGN = 0x8D`
- `SIZE = 0x82, // Returns the length of the input string.`
- `SUB = 0x94, // b is subtracted from a.`
- `SUBSTR = 0x7F, // Returns a section of a string.`
- `SWAP = 0x7C, // The top two items on the stack are swapped.`
- `SYSCALL = 0x41`
- `TAILCALL = 0x69`
- `THROW = 0xF0`
- `THROWIFNOT = 0xF1`
- `TOALTSTACK = 0x6B, // Puts the input onto the top of the alt stack. Removes it from the main stack.`
- `TUCK = 0x7D, // The item at the top of the stack is copied and inserted before the second-to-top item.`
- `UNPACK = 0xC2`
- `VALUES = 0xCD`
- `VERIFY = 0xAD`
- `WITHIN = 0xA5, // Returns 1 if x is within the specified range (left-inclusive), 0 otherwise.`
- `XDROP = 0x6D`
- `XOR = 0x86, // Boolean exclusive or between each bit in the inputs.`
- `XSWAP = 0x72`
- `XTUCK = 0x73`

## PhantasmaPhoenix.InteropChains.Legacy.Neo2.NeoUtils

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Neo2/Utils/NeoUtils.cs`

### Declarations

```csharp
public static class NeoUtils
```

### Methods

```csharp
public static UInt160 ToScriptHash(this byte[] script)
```

```csharp
public static bool IsValidAddress(this string address)
```

```csharp
public static byte[] AES256Decrypt(this byte[] block, byte[] key)
```

```csharp
public static byte[] Hash160(byte[] message)
```

```csharp
public static byte[] HexToBytes(this string value)
```

```csharp
public static byte[] RIPEMD160(this IEnumerable<byte> value)
```

```csharp
public static string ToAddress(this UInt160 scriptHash)
```

```csharp
public static string ToAddressN3(this UInt160 scriptHash)
```

```csharp
public static string ToHexString(this IEnumerable<byte> value)
```

## PhantasmaPhoenix.InteropChains.Legacy.Neo2.RIPEMD160

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Neo2/Utils/RIPEMD160.cs`

### Declarations

```csharp
public class RIPEMD160
```

### Methods

```csharp
public byte[] ComputeHash(byte[] rgb)
```

## PhantasmaPhoenix.InteropChains.Legacy.Neo2.ScriptBuilder

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Neo2/Utils/Script.cs`

### Declarations

```csharp
public class ScriptBuilder : IDisposable
```

### Methods

```csharp
public ScriptBuilder Emit(OpCode op, byte[] arg = null)
```

```csharp
public ScriptBuilder EmitAppCall(UInt160 scriptHash, bool useTailCall = false)
```

```csharp
public ScriptBuilder EmitJump(OpCode op, short offset)
```

```csharp
public ScriptBuilder EmitPush(BigInteger number)
```

```csharp
public ScriptBuilder EmitPush(bool data)
```

```csharp
public ScriptBuilder EmitPush(byte[] data)
```

```csharp
public ScriptBuilder EmitPush(string data)
```

```csharp
public ScriptBuilder EmitSysCall(string api)
```

```csharp
public byte[] ToArray()
```

```csharp
public int Offset => (int)ms.Position;
```

```csharp
public void Dispose()
```

## PhantasmaPhoenix.InteropChains.Legacy.Neo2.UInt160

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Neo2/Utils/UInt160.cs`

### Declarations

```csharp
public class UInt160 : UIntBase, IComparable<UInt160>, IEquatable<UInt160>
```

### Methods

```csharp
public UInt160() : this(null)
```

```csharp
public UInt160(byte[] value) : base(20, value)
```

```csharp
public int CompareTo(UInt160 other)
```

```csharp
public static UInt160 Parse(string value)
```

```csharp
public static bool TryParse(string s, out UInt160 result)
```

```csharp
public static bool operator <(UInt160 left, UInt160 right)
```

```csharp
public static bool operator <=(UInt160 left, UInt160 right)
```

```csharp
public static bool operator >(UInt160 left, UInt160 right)
```

```csharp
public static bool operator >=(UInt160 left, UInt160 right)
```

```csharp
public static readonly UInt160 Zero = new UInt160();
```

## PhantasmaPhoenix.InteropChains.Legacy.Neo2.UIntBase

Source: `PhantasmaPhoenix.InteropChains.Legacy/src/Neo2/Utils/UIntBase.cs`

### Declarations

```csharp
public abstract class UIntBase : IEquatable<UIntBase>
```

### Methods

```csharp
public bool Equals(UIntBase other)
```

```csharp
public byte[] ToArray()
```

```csharp
public int Size => data_bytes.Length;
```

```csharp
public override bool Equals(object obj)
```

```csharp
public override int GetHashCode()
```

```csharp
public override string ToString()
```

```csharp
public static bool operator !=(UIntBase left, UIntBase right)
```

```csharp
public static bool operator ==(UIntBase left, UIntBase right)
```

## PhantasmaPhoenix.Link.LinkServer

Source: `PhantasmaPhoenix.Link/src/LinkServer.cs`

### Declarations

```csharp
public class LinkServer
```

### Methods

```csharp
public Action<Action>? OnUI;
```

```csharp
public Action<string>? OnMessageBack;
```

```csharp
public Action<string>? OnUserMessage;
```

```csharp
public DateTime StartTime { get; private set; }
```

```csharp
public LinkServer(WalletLink walletLink)
```

```csharp
public WalletLink WalletLink { get; private set; }
```

```csharp
public static string GenerateWebSocketKey(string input)
```

```csharp
public void Start()
```

```csharp
public void Stop()
```

```csharp
public void Tick()
```

```csharp
public void WebSocket(string path, Action<WebSocket> handler, params string[] protocols)
```

## PhantasmaPhoenix.Link.WebSockets.BufferPool

Source: `PhantasmaPhoenix.Link/src/WebSockets/BufferPool.cs`

### Declarations

```csharp
public class BufferPool
```

### Methods

```csharp
public BufferPool() : this(DEFAULT_BUFFER_SIZE)
```

```csharp
public BufferPool(int bufferSize)
```

```csharp
public MemoryStream GetBuffer()
```

```csharp
public PublicBufferMemoryStream(byte[] buffer, BufferPool bufferPool) : base(new byte[0])
```

```csharp
public override IAsyncResult BeginRead(byte[] buffer, int offset, int count, AsyncCallback? callback, object? state)
```

```csharp
public override IAsyncResult BeginWrite(byte[] buffer, int offset, int count, AsyncCallback? callback, object? state)
```

```csharp
public override Task CopyToAsync(Stream destination, int bufferSize, CancellationToken cancellationToken)
```

```csharp
public override Task FlushAsync(CancellationToken cancellationToken)
```

```csharp
public override Task WriteAsync(byte[] buffer, int offset, int count, CancellationToken cancellationToken)
```

```csharp
public override Task<int> ReadAsync(byte[] buffer, int offset, int count, CancellationToken cancellationToken)
```

```csharp
public override bool CanRead => _ms.CanRead;
```

```csharp
public override bool CanSeek => _ms.CanSeek;
```

```csharp
public override bool CanTimeout => _ms.CanTimeout;
```

```csharp
public override bool CanWrite => _ms.CanWrite;
```

```csharp
public override bool TryGetBuffer(out ArraySegment<byte> buffer)
```

```csharp
public override byte[] GetBuffer()
```

```csharp
public override byte[] ToArray()
```

```csharp
public override int Capacity { get => _ms.Capacity; set => _ms.Capacity = value; }
```

```csharp
public override int EndRead(IAsyncResult asyncResult)
```

```csharp
public override int Read(byte[] buffer, int offset, int count)
```

```csharp
public override int ReadByte()
```

```csharp
public override int ReadTimeout { get => _ms.ReadTimeout; set => _ms.ReadTimeout = value; }
```

```csharp
public override int WriteTimeout { get => _ms.WriteTimeout; set => _ms.WriteTimeout = value; }
```

```csharp
public override long Length => base.Length;
```

```csharp
public override long Position { get => _ms.Position; set => _ms.Position = value; }
```

```csharp
public override long Seek(long offset, SeekOrigin loc)
```

```csharp
public override void Close()
```

```csharp
public override void EndWrite(IAsyncResult asyncResult)
```

```csharp
public override void Flush()
```

```csharp
public override void SetLength(long value)
```

```csharp
public override void Write(byte[] buffer, int offset, int count)
```

```csharp
public override void WriteByte(byte value)
```

```csharp
public override void WriteTo(Stream stream)
```

## PhantasmaPhoenix.Link.WebSockets.EntityTooLargeException

Source: `PhantasmaPhoenix.Link/src/WebSockets/Exceptions.cs`

### Declarations

```csharp
public class EntityTooLargeException : Exception
```

### Methods

```csharp
public EntityTooLargeException() : base()
```

```csharp
public EntityTooLargeException(string message) : base(message)
```

```csharp
public EntityTooLargeException(string message, Exception inner) : base(message, inner)
```

## PhantasmaPhoenix.Link.WebSockets.InvalidHttpResponseCodeException

Source: `PhantasmaPhoenix.Link/src/WebSockets/Exceptions.cs`

### Declarations

```csharp
public class InvalidHttpResponseCodeException : Exception
```

### Methods

```csharp
public InvalidHttpResponseCodeException() : base()
```

```csharp
public InvalidHttpResponseCodeException(string message) : base(message)
```

```csharp
public InvalidHttpResponseCodeException(string message, Exception inner) : base(message, inner)
```

```csharp
public InvalidHttpResponseCodeException(string responseCode, string responseDetails, string responseHeader) : base(responseCode)
```

```csharp
public string? ResponseCode { get; private set; }
```

```csharp
public string? ResponseDetails { get; private set; }
```

```csharp
public string? ResponseHeader { get; private set; }
```

## PhantasmaPhoenix.Link.WebSockets.SecWebSocketKeyMissingException

Source: `PhantasmaPhoenix.Link/src/WebSockets/Exceptions.cs`

### Declarations

```csharp
public class SecWebSocketKeyMissingException : Exception
```

### Methods

```csharp
public SecWebSocketKeyMissingException() : base()
```

```csharp
public SecWebSocketKeyMissingException(string message) : base(message)
```

```csharp
public SecWebSocketKeyMissingException(string message, Exception inner) : base(message, inner)
```

## PhantasmaPhoenix.Link.WebSockets.ServerListenerSocketException

Source: `PhantasmaPhoenix.Link/src/WebSockets/Exceptions.cs`

### Declarations

```csharp
public class ServerListenerSocketException : Exception
```

### Methods

```csharp
public ServerListenerSocketException() : base()
```

```csharp
public ServerListenerSocketException(string message) : base(message)
```

```csharp
public ServerListenerSocketException(string message, Exception inner) : base(message, inner)
```

## PhantasmaPhoenix.Link.WebSockets.WebSocketBufferOverflowException

Source: `PhantasmaPhoenix.Link/src/WebSockets/Exceptions.cs`

### Declarations

```csharp
public class WebSocketBufferOverflowException : Exception
```

### Methods

```csharp
public WebSocketBufferOverflowException() : base()
```

```csharp
public WebSocketBufferOverflowException(string message) : base(message)
```

```csharp
public WebSocketBufferOverflowException(string message, Exception inner) : base(message, inner)
```

## PhantasmaPhoenix.Link.WebSockets.WebSocketHandshakeFailedException

Source: `PhantasmaPhoenix.Link/src/WebSockets/Exceptions.cs`

### Declarations

```csharp
public class WebSocketHandshakeFailedException : Exception
```

### Methods

```csharp
public WebSocketHandshakeFailedException() : base()
```

```csharp
public WebSocketHandshakeFailedException(string message) : base(message)
```

```csharp
public WebSocketHandshakeFailedException(string message, Exception inner) : base(message, inner)
```

## PhantasmaPhoenix.Link.WebSockets.WebSocketVersionNotSupportedException

Source: `PhantasmaPhoenix.Link/src/WebSockets/Exceptions.cs`

### Declarations

```csharp
public class WebSocketVersionNotSupportedException : Exception
```

### Methods

```csharp
public WebSocketVersionNotSupportedException() : base()
```

```csharp
public WebSocketVersionNotSupportedException(string message) : base(message)
```

```csharp
public WebSocketVersionNotSupportedException(string message, Exception inner) : base(message, inner)
```

## PhantasmaPhoenix.Link.WebSockets.HTTPCode

Source: `PhantasmaPhoenix.Link/src/WebSockets/HTTPRequest.cs`

### Declarations

```csharp
public enum HTTPCode
```

### Variants

- `BadRequest = 400`
- `Forbidden = 403`
- `InternalServerError = 500`
- `NotFound = 404`
- `NotModified = 304`
- `OK = 200`
- `Redirect = 302, //https://en.wikipedia.org/wiki/HTTP_302`
- `ServiceUnavailable = 503`
- `Unauthorized = 401`

## PhantasmaPhoenix.Link.WebSockets.HTTPRequest

Source: `PhantasmaPhoenix.Link/src/WebSockets/HTTPRequest.cs`

### Declarations

```csharp
public class HTTPRequest
```

### Methods

```csharp
public Dictionary<string, string> args = new Dictionary<string, string>();
```

```csharp
public Dictionary<string, string> headers = new Dictionary<string, string>(StringComparer.InvariantCultureIgnoreCase);
```

```csharp
public Method method;
```

```csharp
public bool HasVariable(string name)
```

```csharp
public byte[]? bytes;
```

```csharp
public enum Method
```

```csharp
public string? GetVariable(string name)
```

```csharp
public string? path;
```

```csharp
public string? postBody;
```

```csharp
public string? url;
```

```csharp
public string? version;
```

## PhantasmaPhoenix.Link.WebSockets.WebSocketState

Source: `PhantasmaPhoenix.Link/src/WebSockets/WebSocket.cs`

### Declarations

```csharp
public enum WebSocketState
```

### Variants

- `Aborted = 6        //     Reserved for future use.`
- `CloseReceived = 4,        //     A close message was received from the remote endpoint.`
- `CloseSent = 3,        //     A close message was sent to the remote endpoint.`
- `Closed = 5,        //     Indicates the WebSocket close handshake completed gracefully.`
- `Connecting = 1,        //     The connection is negotiating the handshake with the remote endpoint.`
- `None = 0,        //     Reserved for future use.`
- `Open = 2,        //     The initial state after the HTTP handshake has been completed.`

## PhantasmaPhoenix.Link.WebSockets.WebSocketMessageType

Source: `PhantasmaPhoenix.Link/src/WebSockets/WebSocket.cs`

### Declarations

```csharp
public enum WebSocketMessageType
```

### Variants

- `Binary = 1,        //     The message is in binary format.`
- `Close = 2        //     A receive has completed because a close message was received.`
- `Text = 0,        //     The message is clear text.`

## PhantasmaPhoenix.Link.WebSockets.WebSocketCloseStatus

Source: `PhantasmaPhoenix.Link/src/WebSockets/WebSocket.cs`

### Declarations

```csharp
public enum WebSocketCloseStatus
```

### Variants

- `Empty = 1005`
- `EndpointUnavailable = 1001`
- `InternalServerError = 1011`
- `InvalidMessageType = 1003`
- `InvalidPayloadData = 1007`
- `MandatoryExtension = 1010`
- `MessageTooBig = 1009`
- `None = 0`
- `NormalClosure = 1000`
- `PolicyViolation = 1008`
- `ProtocolError = 1002`

## PhantasmaPhoenix.Link.WebSockets.WebSocketReceiveResult

Source: `PhantasmaPhoenix.Link/src/WebSockets/WebSocket.cs`

### Declarations

```csharp
public struct WebSocketReceiveResult
```

### Methods

```csharp
public WebSocketCloseStatus CloseStatus { get; }
```

```csharp
public WebSocketMessageType MessageType { get; }
```

```csharp
public WebSocketReceiveResult(int count, WebSocketMessageType messageType, bool endOfMessage, ArraySegment<byte> bytes)
```

```csharp
public WebSocketReceiveResult(int count, WebSocketMessageType messageType, bool endOfMessage, WebSocketCloseStatus closeStatus, string? closeStatusDescription)
```

```csharp
public bool EndOfMessage { get; }
```

```csharp
public byte[]? Bytes { get; }
```

```csharp
public int Count { get; }
```

```csharp
public string? CloseStatusDescription { get; }
```

## PhantasmaPhoenix.Link.WebSockets.WebSocket

Source: `PhantasmaPhoenix.Link/src/WebSockets/WebSocket.cs`

### Declarations

```csharp
public class WebSocket
```

### Methods

```csharp
public DateTime LastPingPong { get; private set; }
```

```csharp
public WebSocket(Func<MemoryStream> recycledStreamFactory, Stream stream, int keepAliveInterval, string? secWebSocketExtensions, bool includeExceptionInCloseResponse, bool isClient, string? subProtocol)
```

```csharp
public WebSocketCloseStatus? CloseStatus => _closeStatus;
```

```csharp
public WebSocketReceiveResult Receive()
```

```csharp
public WebSocketState State { get { return _state; } }
```

```csharp
public bool IsOpen => State == WebSocketState.Open;
```

```csharp
public bool NeedsPing { get; private set; }
```

```csharp
public int KeepAliveInterval { get; private set; }
```

```csharp
public string? CloseStatusDescription => _closeStatusDescription;
```

```csharp
public string? SubProtocol => _subProtocol;
```

```csharp
public void Close(WebSocketCloseStatus closeStatus, string statusDescription)
```

```csharp
public void CloseOutput(WebSocketCloseStatus closeStatus, string statusDescription)
```

```csharp
public void Dispose()
```

```csharp
public void Send(ArraySegment<byte> buffer, WebSocketMessageType messageType, bool endOfMessage)
```

```csharp
public void Send(byte[] bytes)
```

```csharp
public void Send(string text)
```

```csharp
public void SendPing()
```

## PhantasmaPhoenix.NFT.IRom

Source: `PhantasmaPhoenix.NFT/src/Abstractions/IRom.cs`

### Declarations

```csharp
public interface IRom
```

## PhantasmaPhoenix.NFT.Extensions.TokenDataExtensions

Source: `PhantasmaPhoenix.NFT/src/Extensions/TokenDataExtensions.cs`

### Declarations

```csharp
public static class TokenDataExtensions
```

### Methods

```csharp
public static IRom ParseRom(this TokenDataResult tokenData, string symbol)
```

```csharp
public static string? GetPropertyValue(this TokenDataResult tokenData, string key)
```

## PhantasmaPhoenix.NFT.CrownRom

Source: `PhantasmaPhoenix.NFT/src/ROM/CrownRom.cs`

### Declarations

```csharp
public class CrownRom : IRom
```

### Methods

```csharp
public (bool, string?) HasParsingError() => (!string.IsNullOrEmpty(parsingError), parsingError);
```

```csharp
public Address staker;
```

```csharp
public CrownRom(byte[] rom, string tokenId)
```

```csharp
public DateTime GetDate() => date;
```

```csharp
public Timestamp date;
```

```csharp
public bool IsEmpty() => isEmpty;
```

```csharp
public string GetDescription() => "";
```

```csharp
public string GetName() => "CROWN #" + tokenId;
```

```csharp
public string tokenId;
```

## PhantasmaPhoenix.NFT.VMDictionaryRom

Source: `PhantasmaPhoenix.NFT/src/ROM/VMDictionaryRom.cs`

### Declarations

```csharp
public class VMDictionaryRom : IRom
```

### Methods

```csharp
public (bool, string?) HasParsingError() => (!string.IsNullOrEmpty(parsingError), parsingError);
```

```csharp
public DateTime GetDate()
```

```csharp
public VMDictionaryRom(byte[] romBytes)
```

```csharp
public bool IsEmpty() => isEmpty;
```

```csharp
public string GetDescription()
```

```csharp
public string GetName()
```

## PhantasmaPhoenix.Protocol.ITransaction

Source: `PhantasmaPhoenix.Protocol/src/Abstractions/ITransaction.cs`

### Declarations

```csharp
public interface ITransaction
```

## PhantasmaPhoenix.Protocol.DomainExtensions

Source: `PhantasmaPhoenix.Protocol/src/DomainExtensions.cs`

### Declarations

```csharp
public static class DomainExtensions
```

### Methods

```csharp
public static T GetContent<T>(this Event evt)
```

## PhantasmaPhoenix.Protocol.DomainSettings

Source: `PhantasmaPhoenix.Protocol/src/DomainSettings.cs`

### Declarations

```csharp
public static class DomainSettings
```

### Methods

```csharp
public const int AddressMaxSize = 34;
```

```csharp
public const int ArgsMax = 64;
```

```csharp
public const int DefaultMinimumGasFee = 100000; // 100000
```

```csharp
public const int FiatTokenDecimals = 8;
```

```csharp
public const int FieldMaxLength = 80;
```

```csharp
public const int FieldMinLength = 1;
```

```csharp
public const int FuelTokenDecimals = 10;
```

```csharp
public const int InitialValidatorCount = 4;
```

```csharp
public const int LatestKnownProtocol = 19;
```

```csharp
public const int LiquidityTokenDecimals = 8;
```

```csharp
public const int MAX_TOKEN_DECIMALS = 18;
```

```csharp
public const int MaxEventsPerBlock = 2048;
```

```csharp
public const int MaxEventsPerTx = 8096;
```

```csharp
public const int MaxOracleEntriesPerBlock = 5120;
```

```csharp
public const int MaxTriggerLoop = 5;
```

```csharp
public const int MaxTxPerBlock = 1024;
```

```csharp
public const int NameMaxLength = 255;
```

```csharp
public const int Phantasma20Protocol = 7;
```

```csharp
public const int Phantasma30Protocol = 8;
```

```csharp
public const int ScriptMaxSize = short.MaxValue;
```

```csharp
public const int StakingTokenDecimals = 8;
```

```csharp
public const int UrlMaxLength = 2048;
```

```csharp
public const string FiatTokenName = "Dollars";
```

```csharp
public const string FiatTokenSymbol = "USD";
```

```csharp
public const string FuelPerContractDeployTag = "nexus.contract.cost";
```

```csharp
public const string FuelPerOrganizationDeployTag = "nexus.organization.cost";
```

```csharp
public const string FuelPerTokenDeployTag = "nexus.token.cost";
```

```csharp
public const string FuelTokenName = "Phantasma Energy";
```

```csharp
public const string FuelTokenSymbol = "KCAL";
```

```csharp
public const string LiquidityTokenName = "Phantasma Liquidity";
```

```csharp
public const string LiquidityTokenSymbol = "LP";
```

```csharp
public const string MastersOrganizationName = "masters";
```

```csharp
public const string NexusMainnet = "mainnet";
```

```csharp
public const string NexusSimnet = "simnet";
```

```csharp
public const string NexusTestnet = "testnet";
```

```csharp
public const string PhantomForceOrganizationName = "phantom_force";
```

```csharp
public const string PlatformName = "phantasma";
```

```csharp
public const string RewardTokenName = "Phantasma Crown";
```

```csharp
public const string RewardTokenSymbol = "CROWN";
```

```csharp
public const string RootChainName = "main";
```

```csharp
public const string StakersOrganizationName = "stakers";
```

```csharp
public const string StakingTokenName = "Phantasma Stake";
```

```csharp
public const string StakingTokenSymbol = "SOUL";
```

```csharp
public const string ValidatorsOrganizationName = "validators";
```

```csharp
public static readonly IEnumerable<string> SystemTokens = new List<string>
```

```csharp
public static readonly int ArchiveMaxSize = 104857600; //100mb
```

```csharp
public static readonly int ArchiveMinSize = 64; // in bytes
```

```csharp
public static readonly string InfusionName = "infusion";
```

## PhantasmaPhoenix.Protocol.EventKind

Source: `PhantasmaPhoenix.Protocol/src/Enums.cs`

### Declarations

```csharp
public enum EventKind
```

### Variants

- `AddressLink = 10`
- `AddressMigration = 46`
- `AddressRegister = 9`
- `AddressUnlink = 11`
- `AddressUnregister = 17`
- `ChainCreate = 1`
- `ChainSwap = 43`
- `ChannelCreate = 36`
- `ChannelRefill = 37`
- `ChannelSettle = 38`
- `ContractDeploy = 45`
- `ContractKill = 60`
- `ContractRegister = 44`
- `ContractUpgrade = 47`
- `Crowdsale = 58`
- `CrownRewards = 56`
- `Custom = 64`
- `Custom_V2 = 65`
- `DomainCreate = 52`
- `DomainDelete = 53`
- `ExecutionFailure = 63`
- `FeedCreate = 22`
- `FeedUpdate = 23`
- `FileCreate = 24`
- `FileDelete = 25`
- `GasEscrow = 15`
- `GasPayment = 16`
- `GovernanceSetChainConfig = 67`
- `GovernanceSetGasConfig = 66`
- `Inflation = 49`
- `Infusion = 57`
- `LeaderboardCreate = 39`
- `LeaderboardInsert = 40`
- `LeaderboardReset = 41`
- `Log = 48`
- `MasterClaim = 62`
- `OrderBid = 59`
- `OrderCancelled = 19`
- `OrderClosed = 21`
- `OrderCreated = 18`
- `OrderFilled = 20`
- `OrganizationAdd = 13`
- `OrganizationCreate = 12`
- `OrganizationKill = 61`
- `OrganizationRemove = 14`
- `OwnerAdded = 50`
- `OwnerRemoved = 51`
- `PackedNFT = 30`
- `PlatformCreate = 42`
- `PollClosed = 34`
- `PollCreated = 33`
- `PollVote = 35`
- `SpecialResolution = 69`
- `TaskStart = 54`
- `TaskStop = 55`
- `TokenBurn = 6`
- `TokenClaim = 8`
- `TokenCreate = 2`
- `TokenMint = 5`
- `TokenReceive = 4`
- `TokenSend = 3`
- `TokenSeriesCreate = 68`
- `TokenStake = 7`
- `Unknown = 0`
- `ValidatorElect = 27`
- `ValidatorPropose = 26`
- `ValidatorRemove = 28`
- `ValidatorSwitch = 29`
- `ValueCreate = 31`
- `ValueUpdate = 32`

## PhantasmaPhoenix.Protocol.ExecutionState

Source: `PhantasmaPhoenix.Protocol/src/Enums.cs`

### Declarations

```csharp
public enum ExecutionState
```

### Variants

- `Break`
- `Fault`
- `Halt`
- `Running`

## PhantasmaPhoenix.Protocol.ProofOfWork

Source: `PhantasmaPhoenix.Protocol/src/Enums.cs`

### Declarations

```csharp
public enum ProofOfWork
```

### Variants

- `Extreme = 30`
- `Hard = 19`
- `Heavy = 24`
- `Minimal = 5`
- `Moderate = 15`
- `None = 0`

## PhantasmaPhoenix.Protocol.NativeContractKind

Source: `PhantasmaPhoenix.Protocol/src/Enums.cs`

### Declarations

```csharp
public enum NativeContractKind
```

### Variants

- `Account`
- `Block`
- `Consensus`
- `Exchange`
- `Friends`
- `Gas`
- `Governance`
- `Interop`
- `Mail`
- `Market`
- `Privacy`
- `Ranking`
- `Relay`
- `Sale`
- `Stake`
- `Storage`
- `Swap`
- `Unknown`
- `Validator`

## PhantasmaPhoenix.Protocol.Nexus

Source: `PhantasmaPhoenix.Protocol/src/Enums.cs`

### Declarations

```csharp
public enum Nexus
```

### Variants

- `Mainnet`
- `Simnet`
- `Testnet`

## PhantasmaPhoenix.Protocol.TokenFlags

Source: `PhantasmaPhoenix.Protocol/src/Enums.cs`

### Declarations

```csharp
public enum TokenFlags
```

### Variants

- `Burnable = 1 << 8`
- `Divisible = 1 << 3`
- `Fiat = 1 << 6`
- `Finite = 1 << 2`
- `Fuel = 1 << 4`
- `Fungible = 1 << 1`
- `None = 0`
- `Stakable = 1 << 5`
- `Swappable = 1 << 7`
- `Transferable = 1 << 0`

## PhantasmaPhoenix.Protocol.TokenStatus

Source: `PhantasmaPhoenix.Protocol/src/Enums.cs`

### Declarations

```csharp
public enum TokenStatus
```

### Variants

- `Active`
- `Infused`

## PhantasmaPhoenix.Protocol.TypeAuction

Source: `PhantasmaPhoenix.Protocol/src/Enums.cs`

### Declarations

```csharp
public enum TypeAuction
```

### Variants

- `Classic = 1`
- `Dutch = 3`
- `Fixed = 0`
- `Reserve = 2`

## PhantasmaPhoenix.Protocol.SaleEventKind

Source: `PhantasmaPhoenix.Protocol/src/Enums.cs`

### Declarations

```csharp
public enum SaleEventKind
```

### Variants

- `AddedToWhitelist`
- `Creation`
- `Distribution`
- `HardCap`
- `Participation`
- `PriceChange`
- `Refund`
- `RemovedFromWhitelist`
- `SoftCap`

## PhantasmaPhoenix.Protocol.Block

Source: `PhantasmaPhoenix.Protocol/src/Structures/Block.cs`

### Declarations

```csharp
public sealed class Block : ISerializable
```

### Methods

```csharp
public Address ChainAddress { get; private set; }
```

```csharp
public Address Validator { get; private set; }
```

```csharp
public BigInteger GetTransactionFee(Hash transactionHash)
```

```csharp
public BigInteger Height { get; private set; }
```

```csharp
public Block()
```

```csharp
public Block(BigInteger height, Address chainAddress, Timestamp timestamp, Hash previousHash, uint protocol, Address validator, byte[] payload, IEnumerable<OracleEntry>? oracleEntries = null)
```

```csharp
public Event[] GetEventsForTransaction(Hash hash)
```

```csharp
public ExecutionState GetStateForTransaction(Hash hash)
```

```csharp
public Hash Hash
```

```csharp
public Hash PreviousHash { get; private set; }
```

```csharp
public Hash[] TransactionHashes => _transactionHashes.ToArray();
```

```csharp
public IEnumerable<Event> Events => _blockEvents;
```

```csharp
public List<OracleEntry> _oracleData = new List<OracleEntry>();
```

```csharp
public OracleEntry[] OracleData => _oracleData.Select(x => (OracleEntry)x).ToArray();
```

```csharp
public Signature Signature { get; private set; }
```

```csharp
public Timestamp Timestamp { get; private set; }
```

```csharp
public bool IsSigned => Signature != null;
```

```csharp
public byte[] GetResultForTransaction(Hash hash)
```

```csharp
public byte[] Payload { get; private set; }
```

```csharp
public byte[] ToByteArray(bool withSignatures)
```

```csharp
public int GetTxIndex(Hash txHash)
```

```csharp
public int TransactionCount => _transactionHashes.Count;
```

```csharp
public static BigInteger GetBlockReward(Block block)
```

```csharp
public static Block Unserialize(BinaryReader reader)
```

```csharp
public static Block Unserialize(byte[] bytes)
```

```csharp
public uint Protocol { get; private set; }
```

```csharp
public void SerializeData(BinaryWriter writer)
```

```csharp
public void UnserializeData(BinaryReader reader)
```

## PhantasmaPhoenix.Protocol.ChainValueEventData

Source: `PhantasmaPhoenix.Protocol/src/Structures/ChainValueEventData.cs`

### Declarations

```csharp
public struct ChainValueEventData
```

### Methods

```csharp
public BigInteger Value;
```

```csharp
public string Name;
```

## PhantasmaPhoenix.Protocol.Event

Source: `PhantasmaPhoenix.Protocol/src/Structures/Event.cs`

### Declarations

```csharp
public struct Event
```

### Methods

```csharp
public Address Address { get; private set; }
```

```csharp
public Event(EventKind kind, Address address, string contract, byte[] data, string? name = null)
```

```csharp
public EventKind Kind { get; private set; }
```

```csharp
public byte[] Data { get; private set; }
```

```csharp
public override bool Equals(object obj)
```

```csharp
public override string ToString()
```

```csharp
public static Event Unserialize(BinaryReader reader)
```

```csharp
public static Event Unserialize(byte[] bytes)
```

```csharp
public string Contract { get; private set; }
```

```csharp
public string? Name { get; private set; }
```

```csharp
public void Serialize(BinaryWriter writer)
```

## PhantasmaPhoenix.Protocol.ExtendedEvents.MarketOrderData

Source: `PhantasmaPhoenix.Protocol/src/Structures/ExtendedEvents/MarketOrderData.cs`

### Declarations

```csharp
public struct MarketOrderData
```

### Methods

```csharp
public MarketOrderData( string baseSymbol, string quoteSymbol, string tokenId, ulong carbonBaseTokenId, ulong carbonQuoteTokenId, ulong carbonInstanceId, string seller, string buyer, string price, string endPrice, long startDate, long endDate, string type)
```

```csharp
public long EndDate;
```

```csharp
public long StartDate;
```

```csharp
public string BaseSymbol;
```

```csharp
public string Buyer;
```

```csharp
public string EndPrice;
```

```csharp
public string Price;
```

```csharp
public string QuoteSymbol;
```

```csharp
public string Seller;
```

```csharp
public string TokenId;
```

```csharp
public string Type;
```

```csharp
public ulong CarbonBaseTokenId;
```

```csharp
public ulong CarbonInstanceId;
```

```csharp
public ulong CarbonQuoteTokenId;
```

## PhantasmaPhoenix.Protocol.ExtendedEvents.SpecialResolutionCall

Source: `PhantasmaPhoenix.Protocol/src/Structures/ExtendedEvents/SpecialResolutionData.cs`

### Declarations

```csharp
public struct SpecialResolutionCall
```

### Methods

```csharp
public Dictionary<string, string>? Arguments;
```

```csharp
public SpecialResolutionCall( uint moduleId, string module, uint methodId, string method, Dictionary<string, string>? arguments = null, SpecialResolutionCall[]? calls = null)
```

```csharp
public SpecialResolutionCall[]? Calls;
```

```csharp
public string Method = string.Empty;
```

```csharp
public string Module = string.Empty;
```

```csharp
public uint MethodId;
```

```csharp
public uint ModuleId;
```

## PhantasmaPhoenix.Protocol.ExtendedEvents.SpecialResolutionData

Source: `PhantasmaPhoenix.Protocol/src/Structures/ExtendedEvents/SpecialResolutionData.cs`

### Declarations

```csharp
public struct SpecialResolutionData
```

### Methods

```csharp
public SpecialResolutionCall[] Calls = Array.Empty<SpecialResolutionCall>();
```

```csharp
public SpecialResolutionData(ulong resolutionId, string? description, SpecialResolutionCall[]? calls = null)
```

```csharp
public string? Description;
```

```csharp
public ulong ResolutionId;
```

## PhantasmaPhoenix.Protocol.ExtendedEvents.TokenCreateData

Source: `PhantasmaPhoenix.Protocol/src/Structures/ExtendedEvents/TokenCreateData.cs`

### Declarations

```csharp
public struct TokenCreateData
```

### Methods

```csharp
public Dictionary<string, string> Metadata;
```

```csharp
public TokenCreateData(string symbol, string maxSupply, uint decimals, bool isNonFungible, UInt64 carbonTokenId, Dictionary<string, string> metadata)
```

```csharp
public UInt64 CarbonTokenId;
```

```csharp
public bool IsNonFungible;
```

```csharp
public string MaxSupply;
```

```csharp
public string Symbol;
```

```csharp
public uint Decimals;
```

## PhantasmaPhoenix.Protocol.ExtendedEvents.TokenMintData

Source: `PhantasmaPhoenix.Protocol/src/Structures/ExtendedEvents/TokenMintData.cs`

### Declarations

```csharp
public struct TokenMintData
```

### Methods

```csharp
public Dictionary<string, string> Metadata;
```

```csharp
public TokenMintData(string symbol, string tokenId, string seriesId, uint mintNumber, ulong carbonTokenId, uint carbonSeriesId, ulong carbonInstanceId, string owner, Dictionary<string, string> metadata)
```

```csharp
public string Owner;
```

```csharp
public string SeriesId;
```

```csharp
public string Symbol;
```

```csharp
public string TokenId;
```

```csharp
public uint CarbonSeriesId;
```

```csharp
public uint MintNumber;
```

```csharp
public ulong CarbonInstanceId;
```

```csharp
public ulong CarbonTokenId;
```

## PhantasmaPhoenix.Protocol.ExtendedEvents.TokenSeriesCreateData

Source: `PhantasmaPhoenix.Protocol/src/Structures/ExtendedEvents/TokenSeriesCreateData.cs`

### Declarations

```csharp
public struct TokenSeriesCreateData
```

### Methods

```csharp
public Dictionary<string, string> Metadata;
```

```csharp
public TokenSeriesCreateData(string symbol, string seriesId, uint maxMint, uint maxSupply, string owner, UInt64 carbonTokenId, UInt32 carbonSeriesId, Dictionary<string, string> metadata)
```

```csharp
public UInt32 CarbonSeriesId;
```

```csharp
public UInt64 CarbonTokenId;
```

```csharp
public string Owner;
```

```csharp
public string SeriesId;
```

```csharp
public string Symbol;
```

```csharp
public uint MaxMint;
```

```csharp
public uint MaxSupply;
```

## PhantasmaPhoenix.Protocol.GasEventData

Source: `PhantasmaPhoenix.Protocol/src/Structures/GasEventData.cs`

### Declarations

```csharp
public struct GasEventData
```

### Methods

```csharp
public GasEventData(Address address, BigInteger price, BigInteger amount)
```

```csharp
public byte[] Serialize()
```

```csharp
public readonly Address address;
```

```csharp
public readonly BigInteger amount;
```

```csharp
public readonly BigInteger price;
```

## PhantasmaPhoenix.Protocol.InfusionEventData

Source: `PhantasmaPhoenix.Protocol/src/Structures/InfusionEventData.cs`

### Declarations

```csharp
public struct InfusionEventData
```

### Methods

```csharp
public InfusionEventData(string baseSymbol, BigInteger tokenID, string infusedSymbol, BigInteger infusedValue, string chainName)
```

```csharp
public readonly BigInteger InfusedValue;
```

```csharp
public readonly BigInteger TokenID;
```

```csharp
public readonly string BaseSymbol;
```

```csharp
public readonly string ChainName;
```

```csharp
public readonly string InfusedSymbol;
```

## PhantasmaPhoenix.Protocol.MarketEventData

Source: `PhantasmaPhoenix.Protocol/src/Structures/MarketEventData.cs`

### Declarations

```csharp
public struct MarketEventData
```

### Methods

```csharp
public BigInteger EndPrice;
```

```csharp
public BigInteger ID;
```

```csharp
public BigInteger Price;
```

```csharp
public TypeAuction Type;
```

```csharp
public string BaseSymbol;
```

```csharp
public string QuoteSymbol;
```

## PhantasmaPhoenix.Protocol.OracleEntry

Source: `PhantasmaPhoenix.Protocol/src/Structures/OracleEntry.cs`

### Declarations

```csharp
public struct OracleEntry
```

### Methods

```csharp
public OracleEntry(string url, byte[] content)
```

```csharp
public byte[] Content { get; private set; }
```

```csharp
public override bool Equals(object obj)
```

```csharp
public override int GetHashCode()
```

```csharp
public string URL { get; private set; }
```

## PhantasmaPhoenix.Protocol.OrganizationEventData

Source: `PhantasmaPhoenix.Protocol/src/Structures/OrganizationEventData.cs`

### Declarations

```csharp
public struct OrganizationEventData
```

### Methods

```csharp
public OrganizationEventData(string organization, Address memberAddress)
```

```csharp
public readonly Address MemberAddress;
```

```csharp
public readonly string Organization;
```

## PhantasmaPhoenix.Protocol.SaleEventData

Source: `PhantasmaPhoenix.Protocol/src/Structures/SaleEventData.cs`

### Declarations

```csharp
public struct SaleEventData
```

### Methods

```csharp
public Hash saleHash;
```

```csharp
public SaleEventKind kind;
```

## PhantasmaPhoenix.Protocol.TokenEventData

Source: `PhantasmaPhoenix.Protocol/src/Structures/TokenEventData.cs`

### Declarations

```csharp
public struct TokenEventData
```

### Methods

```csharp
public TokenEventData(string symbol, BigInteger value, string chainName)
```

```csharp
public byte[] Serialize()
```

```csharp
public readonly BigInteger Value;
```

```csharp
public readonly string ChainName;
```

```csharp
public readonly string Symbol;
```

## PhantasmaPhoenix.Protocol.Transaction

Source: `PhantasmaPhoenix.Protocol/src/Structures/Transaction.cs`

### Declarations

```csharp
public sealed class Transaction : ITransaction, ISerializable
```

### Methods

```csharp
public Hash Hash { get; private set; }
```

```csharp
public Hash Sign(IKeyPair keypair, Func<byte[], byte[], byte[], byte[]>? customSignFunction = null)
```

```csharp
public Signature GetTransactionSignature(IKeyPair keypair, Func<byte[], byte[], byte[], byte[]>? customSignFunction = null)
```

```csharp
public Signature[] Signatures { get; private set; }
```

```csharp
public Timestamp Expiration { get; private set; }
```

```csharp
public Transaction( string nexusName, string chainName, byte[] script, Timestamp expiration, Address gasPayer, Address gasTarget, BigInteger gasLimit, BigInteger gasPrice, byte[]? payload = null)
```

```csharp
public Transaction( string nexusName, string chainName, byte[] script, Timestamp expiration, Address gasPayer, Address gasTarget, BigInteger gasLimit, BigInteger gasPrice, string payload) : this(nexusName, chainName, script, expiration, gasPayer, gasTarget, gasLimit, gasPrice, Encoding.UTF8.GetBytes(payload))
```

```csharp
public Transaction( string nexusName, string chainName, byte[] script, Timestamp expiration, byte[]? payload = null)
```

```csharp
public Transaction( string nexusName, string chainName, byte[] script, Timestamp expiration, string payload) : this(nexusName, chainName, script, expiration, Encoding.UTF8.GetBytes(payload))
```

```csharp
public Transaction()
```

```csharp
public bool HasSignatures => Signatures != null && Signatures.Length > 0;
```

```csharp
public bool IsSignedBy(Address address)
```

```csharp
public bool IsSignedBy(IEnumerable<Address> addresses)
```

```csharp
public bool IsSignedByEveryone(IEnumerable<Address> addresses)
```

```csharp
public bool ValidateNexus(Nexus chainNexus)
```

```csharp
public byte[] Payload { get; private set; }
```

```csharp
public byte[] Script { get; private set; }
```

```csharp
public byte[] ToByteArray(bool withSignature)
```

```csharp
public override bool Equals(object obj)
```

```csharp
public override string ToString()
```

```csharp
public readonly static Transaction? Null = null;
```

```csharp
public static BigInteger GetTransactionFee(Hash transactionHash, Block block)
```

```csharp
public static Transaction? Unserialize(BinaryReader reader)
```

```csharp
public static Transaction? Unserialize(byte[] bytes)
```

```csharp
public static byte[] GetMessageHash(byte[] message)
```

```csharp
public static readonly int DefaultGasLimit = 9999;
```

```csharp
public string ChainName { get; private set; }
```

```csharp
public string NexusName { get; private set; }
```

```csharp
public void AddSignature(Signature signature)
```

```csharp
public void Mine(int targetDifficulty)
```

```csharp
public void Serialize(BinaryWriter writer, bool withSignature)
```

```csharp
public void SerializeData(BinaryWriter writer)
```

```csharp
public void UnserializeData(BinaryReader reader)
```

## PhantasmaPhoenix.Protocol.TransactionSettleEventData

Source: `PhantasmaPhoenix.Protocol/src/Structures/TransactionSettleEventData.cs`

### Declarations

```csharp
public struct TransactionSettleEventData
```

### Methods

```csharp
public TransactionSettleEventData(Hash hash, string platform, string chain)
```

```csharp
public readonly Hash Hash;
```

```csharp
public readonly string Chain;
```

```csharp
public readonly string Platform;
```

## PhantasmaPhoenix.Protocol.ValidationUtils

Source: `PhantasmaPhoenix.Protocol/src/ValidationUtils.cs`

### Declarations

```csharp
public static class ValidationUtils
```

### Methods

```csharp
public readonly static string ENTRY_CONTEXT_NAME = "entry";
```

```csharp
public static bool IsReservedIdentifier(string name)
```

```csharp
public static bool IsValidIdentifier(string name)
```

```csharp
public static bool IsValidTicker(string name)
```

```csharp
public static readonly string ANONYMOUS_NAME = "anonymous";
```

```csharp
public static readonly string GENESIS_NAME = "genesis";
```

```csharp
public static readonly string NULL_NAME = "null";
```

```csharp
public static string[] prefixNames = new string[]
```

```csharp
public static string[] reservedNames = new string[]
```

## PhantasmaPhoenix.Protocol.IAPIResult

Source: `PhantasmaPhoenix.Protocol/src/WalletLink/IAPIResult.cs`

### Declarations

```csharp
public interface IAPIResult
```

## PhantasmaPhoenix.Protocol.ErrorResult

Source: `PhantasmaPhoenix.Protocol/src/WalletLink/IAPIResult.cs`

### Declarations

```csharp
public struct ErrorResult : IAPIResult
```

### Methods

```csharp
public string error;
```

## PhantasmaPhoenix.Protocol.SingleResult

Source: `PhantasmaPhoenix.Protocol/src/WalletLink/IAPIResult.cs`

### Declarations

```csharp
public struct SingleResult : IAPIResult
```

### Methods

```csharp
public object value;
```

## PhantasmaPhoenix.Protocol.ArrayResult

Source: `PhantasmaPhoenix.Protocol/src/WalletLink/IAPIResult.cs`

### Declarations

```csharp
public struct ArrayResult : IAPIResult
```

### Methods

```csharp
public object[] values;
```

## PhantasmaPhoenix.Protocol.APIUtils

Source: `PhantasmaPhoenix.Protocol/src/WalletLink/IAPIResult.cs`

### Declarations

```csharp
public static class APIUtils
```

### Methods

```csharp
public static JToken FromAPIResult(IAPIResult input)
```

## PhantasmaPhoenix.Protocol.WalletStatus

Source: `PhantasmaPhoenix.Protocol/src/WalletLink/WalletLink.cs`

### Declarations

```csharp
public enum WalletStatus
```

### Variants

- `Closed`
- `Ready`

## PhantasmaPhoenix.Protocol.WalletLink

Source: `PhantasmaPhoenix.Protocol/src/WalletLink/WalletLink.cs`

### Declarations

```csharp
public abstract class WalletLink
```

### Methods

```csharp
public Balance[] balances;
```

```csharp
public Connection(string token, int version)
```

```csharp
public File[] files;
```

```csharp
public WalletLink()
```

```csharp
public abstract string Name { get; }
```

```csharp
public abstract string Nexus { get; }
```

```csharp
public bool success;
```

```csharp
public class Connection
```

```csharp
public const int LinkProtocol = 4;
```

```csharp
public const int WebSocketPort = 7090;
```

```csharp
public int size;
```

```csharp
public int version;
```

```csharp
public readonly int Version;
```

```csharp
public readonly string Token;
```

```csharp
public string address;
```

```csharp
public string alias;
```

```csharp
public string avatar;
```

```csharp
public string dapp;
```

```csharp
public string external;
```

```csharp
public string hash;
```

```csharp
public string message;
```

```csharp
public string name;
```

```csharp
public string nexus;
```

```csharp
public string peer;
```

```csharp
public string platform;
```

```csharp
public string random;
```

```csharp
public string result; // deprecated
```

```csharp
public string signature;
```

```csharp
public string symbol;
```

```csharp
public string token;
```

```csharp
public string value;
```

```csharp
public string version;
```

```csharp
public string wallet;
```

```csharp
public string[] ids;
```

```csharp
public string[] results;
```

```csharp
public struct Account : IAPIResult
```

```csharp
public struct Authorization : IAPIResult
```

```csharp
public struct Balance : IAPIResult
```

```csharp
public struct Error : IAPIResult
```

```csharp
public struct File : IAPIResult
```

```csharp
public struct Invocation : IAPIResult
```

```csharp
public struct MultiSig : IAPIResult
```

```csharp
public struct N3Address : IAPIResult
```

```csharp
public struct NexusResult : IAPIResult
```

```csharp
public struct Peer : IAPIResult
```

```csharp
public struct Signature : IAPIResult
```

```csharp
public struct Transaction : IAPIResult
```

```csharp
public struct WalletVersion : IAPIResult
```

```csharp
public uint date;
```

```csharp
public uint decimals;
```

```csharp
public void Execute(string cmd, Action<int, JToken, bool> callback)
```

```csharp
public void Revoke(string dapp, string token)
```

## PhantasmaPhoenix.Protocol.Carbon.ICarbonBlob

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Abstractions/ICarbonBlob.cs`

### Declarations

```csharp
public interface ICarbonBlob
```

### Methods

```csharp
public void Read(BinaryReader r);
```

```csharp
public void Write(BinaryWriter w);
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxTypes

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Enums/Blockchain/Enums.cs`

### Declarations

```csharp
public enum TxTypes
```

### Variants

- `BurnFungible = 10`
- `BurnFungible_GasPayer = 11`
- `BurnNonFungible = 13`
- `BurnNonFungible_GasPayer = 14`
- `Call = 0`
- `Call_Multi = 1`
- `MintFungible = 9`
- `MintNonFungible = 12`
- `Phantasma = 15`
- `Phantasma_Raw = 16`
- `Trade = 2`
- `TransferFungible = 3`
- `TransferFungible_GasPayer = 4`
- `TransferNonFungible_Multi = 7`
- `TransferNonFungible_Multi_GasPayer = 8`
- `TransferNonFungible_Single = 5`
- `TransferNonFungible_Single_GasPayer = 6`

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.ModuleId

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Enums/Blockchain/Modules/Enums.cs`

### Declarations

```csharp
public enum ModuleId : uint
```

### Variants

- `Governance = 0u`
- `Internal = 0xFFFFFFFFu, // C++'s ~0U`
- `Market = 4u`
- `Organization = 3u`
- `PhantasmaVm = 2u`
- `Token = 1u`

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.TokenFlags

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Enums/Blockchain/Modules/Enums.cs`

### Declarations

```csharp
public enum TokenFlags
```

### Variants

- `BigFungible = 1 << 0`
- `NonFungible = 1 << 1`
- `None = 0`

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.TokensConfigFlags

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Enums/Blockchain/Modules/Enums.cs`

### Declarations

```csharp
public enum TokensConfigFlags
```

### Variants

- `AllowExplicitNftMetaIdMint = 1 << 4`
- `None = 0`
- `RequireMetadata = 1 << 0`
- `RequireNftMetaId = 1 << 2`
- `RequireNftStandard = 1 << 3`
- `RequireSymbol = 1 << 1`

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.TokenContract_Methods

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Enums/Blockchain/Modules/Enums.cs`

### Declarations

```csharp
public enum TokenContract_Methods
```

### Variants

- `ApplyInflation = 22`
- `BurnFungible = 4`
- `BurnNonFungible = 9`
- `CreateMintedTokenSeries = 21`
- `CreateToken = 2`
- `CreateTokenSeries = 6`
- `DeleteTokenSeries = 7`
- `GetBalance = 5`
- `GetBalances = 20`
- `GetInstances = 10`
- `GetNextTokenInflation = 24`
- `GetNonFungibleInfo = 11`
- `GetNonFungibleInfoByRomId = 12`
- `GetSeriesInfo = 13`
- `GetSeriesInfoByMetaId = 14`
- `GetSeriesSupply = 18`
- `GetTokenIdBySymbol = 19`
- `GetTokenInfo = 15`
- `GetTokenInfoBySymbol = 16`
- `GetTokenSupply = 17`
- `MintFungible = 3`
- `MintNonFungible = 8`
- `MintPhantasmaNonFungible = 27`
- `SetTokensConfig = 25`
- `TransferFungible = 0`
- `TransferNonFungible = 1`
- `UpdateSeriesMetadata = 26`
- `UpdateTokenMetadata = 23`

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.MarketContract_Methods

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Enums/Blockchain/Modules/Enums.cs`

### Declarations

```csharp
public enum MarketContract_Methods
```

### Variants

- `BuyToken = 4`
- `BuyTokenById = 5`
- `CancelSale = 2`
- `CancelSaleById = 3`
- `GetTokenListingCount = 6`
- `GetTokenListingInfo = 7`
- `GetTokenListingInfoById = 8`
- `SellToken = 0`
- `SellTokenById = 1`

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Vm.VmType

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Enums/Blockchain/Vm/Enums.cs`

### Declarations

```csharp
public enum VmType
```

### Variants

- `Array = 1`
- `Array_Bytes = Array | Bytes`
- `Array_Bytes16 = Array | Bytes16`
- `Array_Bytes32 = Array | Bytes32`
- `Array_Bytes64 = Array | Bytes64`
- `Array_Dynamic = Array | Dynamic`
- `Array_Int16 = Array | Int16`
- `Array_Int256 = Array | Int256`
- `Array_Int32 = Array | Int32`
- `Array_Int64 = Array | Int64`
- `Array_Int8 = Array | Int8`
- `Array_String = Array | String`
- `Array_Struct = Array | Struct`
- `Bytes = 1 << 1`
- `Bytes16 = 8 << 1`
- `Bytes32 = 9 << 1`
- `Bytes64 = 10 << 1`
- `Dynamic = 0`
- `Int16 = 4 << 1`
- `Int256 = 7 << 1`
- `Int32 = 5 << 1`
- `Int64 = 6 << 1`
- `Int8 = 3 << 1`
- `String = 11 << 1`
- `Struct = 2 << 1`

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Vm.VmException

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Exceptions/Blockchain/Vm/VmException.cs`

### Declarations

```csharp
public class VmException : Exception
```

### Methods

```csharp
public VmException(string message) : base(message) { }
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders.IdHelper

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/Modules/Builders/IdHelper.cs`

### Declarations

```csharp
public static class IdHelper
```

### Methods

```csharp
public static BigInteger GetRandomPhantasmaId()
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders.MetadataField

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/Modules/Builders/MetadataHelper.cs`

### Declarations

```csharp
public sealed class MetadataField
```

### Methods

```csharp
public MetadataField(string name, object? value)
```

```csharp
public object? Value { get; set; }
```

```csharp
public string Name { get; set; }
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders.FieldType

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/Modules/Builders/MetadataHelper.cs`

### Declarations

```csharp
public readonly struct FieldType
```

### Methods

```csharp
public FieldType(string name, VmType type)
```

```csharp
public VmType Type { get; }
```

```csharp
public string Name { get; }
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders.MetadataHelper

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/Modules/Builders/MetadataHelper.cs`

### Declarations

```csharp
public static class MetadataHelper
```

### Methods

```csharp
public static MetadataField? FindMetadataField(IReadOnlyList<MetadataField> fields, string name)
```

```csharp
public static byte[] GetOptionalBytesField(IReadOnlyList<MetadataField> fields, string name)
```

```csharp
public static readonly FieldType[] NftDefaultMetadataFields =
```

```csharp
public static readonly FieldType[] SeriesDefaultMetadataFields =
```

```csharp
public static readonly FieldType[] StandardMetadataFields =
```

```csharp
public static void PushMetadataField( VmNamedVariableSchema fieldSchema, List<VmNamedDynamicVariable> fields, IReadOnlyList<MetadataField> metadataFields)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders.NftRomBuilder

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/Modules/Builders/NftRomBuilder.cs`

### Declarations

```csharp
public static class NftRomBuilder
```

### Methods

```csharp
public static byte[] BuildAndSerialize( VmStructSchema nftRomSchema, BigInteger phantasmaNftId, IReadOnlyList<MetadataField> metadata)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders.PhantasmaNftRomBuilder

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/Modules/Builders/PhantasmaNftRomBuilder.cs`

### Declarations

```csharp
public static class PhantasmaNftRomBuilder
```

### Methods

```csharp
public static VmStructSchema BuildPublicMintSchema(VmStructSchema nftRomSchema)
```

```csharp
public static byte[] BuildAndSerialize( VmStructSchema nftRomSchema, IReadOnlyList<MetadataField> metadata)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders.SeriesInfoBuilder

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/Modules/Builders/SeriesInfoBuilder.cs`

### Declarations

```csharp
public static class SeriesInfoBuilder
```

### Methods

```csharp
public static SeriesInfo Build(BigInteger phantasmaSeriesId, uint maxMint, uint maxSupply, Bytes32 ownerPublicKey, byte[]? metadata = null)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders.TokenInfoBuilder

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/Modules/Builders/TokenInfoBuilder.cs`

### Declarations

```csharp
public static class TokenInfoBuilder
```

### Methods

```csharp
public static TokenInfo Build( string symbol, IntX maxSupply, bool isNFT, uint decimals, Bytes32 creatorPublicKey, byte[]? metadata = null, byte[]? tokenSchemas = null)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders.TokenMetadataBuilder

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/Modules/Builders/TokenMetadataBuilder.cs`

### Declarations

```csharp
public static class TokenMetadataBuilder
```

### Methods

```csharp
public static byte[] BuildAndSerialize(Dictionary<string, string> fields)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders.TokenSchemasBuilder

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/Modules/Builders/TokenSchemasBuilder.cs`

### Declarations

```csharp
public static class TokenSchemasBuilder
```

### Methods

```csharp
public static (bool ok, string? error) Verify(TokenSchemas schemas)
```

```csharp
public static TokenSchemas FromJson(string json)
```

```csharp
public static TokenSchemas PrepareStandardTokenSchemas(bool sharedMetadata = false)
```

```csharp
public static TokenSchemasJson ParseTokenSchemasJson(string json)
```

```csharp
public static byte[] BuildAndSerialize(TokenSchemas? tokenSchemas)
```

```csharp
public static byte[] Serialize(TokenSchemas tokenSchemas)
```

```csharp
public static string SerializeHex(TokenSchemas tokenSchemas)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders.TokenSchemasJson

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/Modules/Builders/TokenSchemasBuilder.cs`

### Declarations

```csharp
public sealed class TokenSchemasJson
```

### Methods

```csharp
public IReadOnlyList<FieldType> Ram { get; set; } = Array.Empty<FieldType>();
```

```csharp
public IReadOnlyList<FieldType> Rom { get; set; } = Array.Empty<FieldType>();
```

```csharp
public IReadOnlyList<FieldType> SeriesMetadata { get; set; } = Array.Empty<FieldType>();
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.Builders.TokenSeriesMetadataBuilder

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/Modules/Builders/TokenSeriesMetadataBuilder.cs`

### Declarations

```csharp
public static class TokenSeriesMetadataBuilder
```

### Methods

```csharp
public static byte[] BuildAndSerialize( VmStructSchema seriesMetadataSchema, BigInteger newPhantasmaSeriesId, IReadOnlyList<MetadataField> metadata)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers.CreateTokenSeriesTxHelper

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/TxHelpers/CreateTokenSeriesTxHelper.cs`

### Declarations

```csharp
public static class CreateTokenSeriesTxHelper
```

### Methods

```csharp
public static TxMsg BuildTx(ulong tokenId, SeriesInfo seriesInfo, Bytes32 creatorPublicKey, CreateSeriesFeeOptions? feeOptions = null, ulong? maxData = null, long? expiry = null)
```

```csharp
public static byte[] BuildTxAndSign(ulong tokenId, SeriesInfo seriesInfo, PhantasmaKeys signer, CreateSeriesFeeOptions? feeOptions = null, ulong? maxData = null, long? expiry = null)
```

```csharp
public static string BuildTxAndSignHex(ulong tokenId, SeriesInfo seriesInfo, PhantasmaKeys signer, CreateSeriesFeeOptions? feeOptions = null, ulong? maxData = null, long? expiry = null)
```

```csharp
public static uint ParseResult(string resultHex)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers.CreateTokenTxHelper

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/TxHelpers/CreateTokenTxHelper.cs`

### Declarations

```csharp
public static class CreateTokenTxHelper
```

### Methods

```csharp
public static TxMsg BuildTx(TokenInfo tokenInfo, Bytes32 creatorPublicKey, CreateTokenFeeOptions? feeOptions = null, ulong? maxData = null, long? expiry = null)
```

```csharp
public static byte[] BuildTxAndSign(TokenInfo tokenInfo, PhantasmaKeys signer, CreateTokenFeeOptions? feeOptions = null, ulong? maxData = null, long? expiry = null)
```

```csharp
public static string BuildTxAndSignHex(TokenInfo tokenInfo, PhantasmaKeys signer, CreateTokenFeeOptions? feeOptions = null, ulong? maxData = null, long? expiry = null)
```

```csharp
public static ulong ParseResult(string resultHex)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers.IFeeOptions

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/TxHelpers/FeeOptions.cs`

### Declarations

```csharp
public interface IFeeOptions
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers.FeeOptions

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/TxHelpers/FeeOptions.cs`

### Declarations

```csharp
public class FeeOptions : IFeeOptions
```

### Methods

```csharp
public FeeOptions(ulong gasFeeBase = 10_000UL, ulong feeMultiplier = 1_000UL)
```

```csharp
public ulong FeeMultiplier { get; }
```

```csharp
public ulong GasFeeBase { get; }
```

```csharp
public virtual ulong CalculateMaxGas(params object[] args)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers.CreateTokenFeeOptions

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/TxHelpers/FeeOptions.cs`

### Declarations

```csharp
public class CreateTokenFeeOptions : FeeOptions, IFeeOptions
```

### Methods

```csharp
public CreateTokenFeeOptions( ulong gasFeeBase = 10_000UL, ulong gasFeeCreateTokenBase = 10_000_000_000UL, ulong gasFeeCreateTokenSymbol = 10_000_000_000UL, ulong feeMultiplier = 10_000UL) : base(gasFeeBase, feeMultiplier)
```

```csharp
public override ulong CalculateMaxGas(params object[] args)
```

```csharp
public ulong GasFeeCreateTokenBase { get; }
```

```csharp
public ulong GasFeeCreateTokenSymbol { get; }
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers.CreateSeriesFeeOptions

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/TxHelpers/FeeOptions.cs`

### Declarations

```csharp
public class CreateSeriesFeeOptions : FeeOptions, IFeeOptions
```

### Methods

```csharp
public CreateSeriesFeeOptions( ulong gasFeeBase = 10_000UL, ulong gasFeeCreateSeriesBase = 2_500_000_000UL, ulong feeMultiplier = 10_000UL) : base(gasFeeBase, feeMultiplier)
```

```csharp
public override ulong CalculateMaxGas(params object[] args)
```

```csharp
public ulong GasFeeCreateSeriesBase { get; }
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers.MintNftFeeOptions

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/TxHelpers/FeeOptions.cs`

### Declarations

```csharp
public class MintNftFeeOptions : FeeOptions, IFeeOptions
```

### Methods

```csharp
public MintNftFeeOptions(ulong gasFeeBase = 10_000UL, ulong feeMultiplier = 1_000UL) : base(gasFeeBase, feeMultiplier) { }
```

```csharp
public override ulong CalculateMaxGas(params object[] args)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers.MintNonFungibleTxHelper

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/TxHelpers/MintNonFungibleTxHelper.cs`

### Declarations

```csharp
public static class MintNonFungibleTxHelper
```

### Methods

```csharp
public static TxMsg BuildTx( ulong tokenId, uint seriesId, Bytes32 senderPublicKey, Bytes32 receiverPublicKey, byte[] rom, byte[]? ram, MintNftFeeOptions? feeOptions = null, ulong? maxData = null, long? expiry = null)
```

```csharp
public static byte[] BuildTxAndSign( ulong tokenId, uint seriesId, PhantasmaKeys signer, Bytes32 receiverPublicKey, byte[] rom, byte[]? ram, MintNftFeeOptions? feeOptions = null, ulong? maxData = null, long? expiry = null)
```

```csharp
public static string BuildTxAndSignHex( ulong tokenId, uint seriesId, PhantasmaKeys signer, Bytes32 receiverPublicKey, byte[] rom, byte[]? ram, MintNftFeeOptions? feeOptions = null, ulong? maxData = null, long? expiry = null)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxHelpers.MintPhantasmaNonFungibleTxHelper

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/TxHelpers/MintPhantasmaNonFungibleTxHelper.cs`

### Declarations

```csharp
public static class MintPhantasmaNonFungibleTxHelper
```

### Methods

```csharp
public static PhantasmaNftMintResult[] ParseResult(string resultHex)
```

```csharp
public static TxMsg BuildTx( ulong tokenId, BigInteger phantasmaSeriesId, Bytes32 senderPublicKey, Bytes32 receiverPublicKey, byte[] publicRom, byte[]? ram, MintNftFeeOptions? feeOptions = null, ulong? maxData = null, long? expiry = null)
```

```csharp
public static TxMsg BuildTx( ulong tokenId, Bytes32 senderPublicKey, Bytes32 receiverPublicKey, PhantasmaNftMintInfo[] tokens, MintNftFeeOptions? feeOptions = null, ulong? maxData = null, long? expiry = null)
```

```csharp
public static byte[] BuildTxAndSign( ulong tokenId, BigInteger phantasmaSeriesId, PhantasmaKeys signer, Bytes32 receiverPublicKey, byte[] publicRom, byte[]? ram, MintNftFeeOptions? feeOptions = null, ulong? maxData = null, long? expiry = null)
```

```csharp
public static byte[] BuildTxAndSign( ulong tokenId, PhantasmaNftMintInfo[] tokens, PhantasmaKeys signer, Bytes32 receiverPublicKey, MintNftFeeOptions? feeOptions = null, ulong? maxData = null, long? expiry = null)
```

```csharp
public static string BuildTxAndSignHex( ulong tokenId, BigInteger phantasmaSeriesId, PhantasmaKeys signer, Bytes32 receiverPublicKey, byte[] publicRom, byte[]? ram, MintNftFeeOptions? feeOptions = null, ulong? maxData = null, long? expiry = null)
```

```csharp
public static string BuildTxAndSignHex( ulong tokenId, PhantasmaNftMintInfo[] tokens, PhantasmaKeys signer, Bytes32 receiverPublicKey, MintNftFeeOptions? feeOptions = null, ulong? maxData = null, long? expiry = null)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsgSigner

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/TxMsgSigner.cs`

### Declarations

```csharp
public static class TxMsgSigner
```

### Methods

```csharp
public static byte[] Sign(TxMsg msg, PhantasmaKeys keys)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Vm.VmGlobal

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Helpers/Blockchain/Vm/VmGlobal.cs`

### Declarations

```csharp
public static class VmGlobal
```

### Methods

```csharp
public static void VmAssert( #if NET6_0_OR_GREATER #endif bool condition, string constraintName = "")
```

```csharp
public static void VmError(string constraintName)
```

```csharp
public static void VmExpect( #if NET6_0_OR_GREATER #endif bool condition, string constraintName)
```

## PhantasmaPhoenix.Protocol.Carbon.BinaryStreamExt

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Serialization/Serialization.cs`

### Declarations

```csharp
public static class BinaryStreamExt
```

### Methods

```csharp
public static BigInteger ReadBigInt(this BinaryReader r)
```

```csharp
public static BigInteger ReadBigInt(this BinaryReader r, out BigInteger data, int preReadHeader = -1)
```

```csharp
public static BigInteger ReadBigInt(this byte[] data)
```

```csharp
public static BigInteger[] ReadArrayBigInt(this BinaryReader r)
```

```csharp
public static Byte Read1(this BinaryReader r)
```

```csharp
public static Bytes16 Read16(this BinaryReader r)
```

```csharp
public static Bytes32 Read32(this BinaryReader r)
```

```csharp
public static Bytes64 Read64(this BinaryReader r)
```

```csharp
public static Int16 Read2(this BinaryReader r)
```

```csharp
public static Int16[] ReadArray16(this BinaryReader r)
```

```csharp
public static Int16[] ReadArray16(this BinaryReader r, out Int16[] data)
```

```csharp
public static Int32 Read4(this BinaryReader r)
```

```csharp
public static Int32[] ReadArray32(this BinaryReader r)
```

```csharp
public static Int32[] ReadArray32(this BinaryReader r, out Int32[] data)
```

```csharp
public static Int64 Read8(this BinaryReader r)
```

```csharp
public static Int64[] ReadArray64(this BinaryReader r)
```

```csharp
public static Int64[] ReadArray64(this BinaryReader r, out Int64[] data)
```

```csharp
public static T Read<T>(this BinaryReader r) where T : ICarbonBlob, new()
```

```csharp
public static T[] ReadArray<T>(this BinaryReader r) where T : ICarbonBlob
```

```csharp
public static byte[] ReadArray(this BinaryReader r)
```

```csharp
public static byte[] ReadExactly(this BinaryReader r, int count)
```

```csharp
public static byte[] ReadRemaining(this BinaryReader r)
```

```csharp
public static byte[][] ReadArrayArray(this BinaryReader r)
```

```csharp
public static sbyte[] ReadArray8(this BinaryReader r)
```

```csharp
public static sbyte[] ReadArray8(this BinaryReader r, out sbyte[] data)
```

```csharp
public static string ReadSz(this BinaryReader r)
```

```csharp
public static string[] ReadArraySz(this BinaryReader r)
```

```csharp
public static void Read1(this BinaryReader r, out Byte v)
```

```csharp
public static void Read16(this BinaryReader r, out Bytes16 v)
```

```csharp
public static void Read16(this BinaryReader r, out byte[] v)
```

```csharp
public static void Read1<T>(this BinaryReader r, out T v) where T : struct
```

```csharp
public static void Read2(this BinaryReader r, out Int16 v)
```

```csharp
public static void Read32(this BinaryReader r, out Bytes32 v)
```

```csharp
public static void Read32(this BinaryReader r, out byte[] v)
```

```csharp
public static void Read4(this BinaryReader r, out Int32 v)
```

```csharp
public static void Read4(this BinaryReader r, out UInt32 v)
```

```csharp
public static void Read4<T>(this BinaryReader r, out T v) where T : struct
```

```csharp
public static void Read64(this BinaryReader r, out Bytes64 v)
```

```csharp
public static void Read64(this BinaryReader r, out byte[] v)
```

```csharp
public static void Read8(this BinaryReader r, out Int64 v)
```

```csharp
public static void Read8(this BinaryReader r, out UInt64 v)
```

```csharp
public static void Read<T>(this BinaryReader r, out T data) where T : ICarbonBlob, new()
```

```csharp
public static void ReadArray(this BinaryReader r, out byte[] data)
```

```csharp
public static void ReadArray(this BinaryReader r, out byte[][] data)
```

```csharp
public static void ReadArray64(this BinaryReader r, out UInt64[] data)
```

```csharp
public static void ReadArray<T>(this BinaryReader r, out T[] data) where T : ICarbonBlob
```

```csharp
public static void ReadSz(this BinaryReader r, out string data)
```

```csharp
public static void Write1(this BinaryWriter w, Byte data)
```

```csharp
public static void Write16(this BinaryWriter w, Bytes16 data)
```

```csharp
public static void Write16(this BinaryWriter w, byte[] data)
```

```csharp
public static void Write1<T>(this BinaryWriter w, T data) where T : IComparable, IFormattable, IConvertible
```

```csharp
public static void Write2(this BinaryWriter w, Int16 data)
```

```csharp
public static void Write32(this BinaryWriter w, Bytes32 data)
```

```csharp
public static void Write32(this BinaryWriter w, byte[] data)
```

```csharp
public static void Write4(this BinaryWriter w, Int32 data)
```

```csharp
public static void Write4(this BinaryWriter w, UInt32 data)
```

```csharp
public static void Write4<T>(this BinaryWriter w, T data) where T : IComparable, IFormattable, IConvertible
```

```csharp
public static void Write64(this BinaryWriter w, Bytes64 data)
```

```csharp
public static void Write64(this BinaryWriter w, byte[] data)
```

```csharp
public static void Write8(this BinaryWriter w, Int64 data)
```

```csharp
public static void Write8(this BinaryWriter w, UInt64 data)
```

```csharp
public static void Write<T>(this BinaryWriter w, T data) where T : ICarbonBlob
```

```csharp
public static void WriteArray(this BinaryWriter w, byte[] data)
```

```csharp
public static void WriteArray(this BinaryWriter w, byte[][] data)
```

```csharp
public static void WriteArray16(this BinaryWriter w, Int16[] data)
```

```csharp
public static void WriteArray32(this BinaryWriter w, Int32[] data)
```

```csharp
public static void WriteArray64(this BinaryWriter w, Int64[] data)
```

```csharp
public static void WriteArray64(this BinaryWriter w, UInt64[] data)
```

```csharp
public static void WriteArray8(this BinaryWriter w, sbyte[] data)
```

```csharp
public static void WriteArray<T>(this BinaryWriter w, T[] data) where T : ICarbonBlob
```

```csharp
public static void WriteArrayBigInt(this BinaryWriter w, BigInteger[] data)
```

```csharp
public static void WriteArraySz(this BinaryWriter w, string[] data)
```

```csharp
public static void WriteBigInt(this BinaryWriter w, BigInteger data)
```

```csharp
public static void WriteBigInt(this BinaryWriter w, byte[] bytes)
```

```csharp
public static void WriteExactly(this BinaryWriter w, byte[] data, int count)
```

```csharp
public static void WriteSz(this BinaryWriter w, string data)
```

## PhantasmaPhoenix.Protocol.Carbon.GenericCastTo

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Serialization/Serialization.cs`

### Declarations

```csharp
public static class GenericCastTo<T>
```

### Methods

```csharp
public static T From<S>(S s)
```

```csharp
public static readonly Func<S, T> caster = Get();
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.ChainConfig

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/ChainConfig.cs`

### Declarations

```csharp
public struct ChainConfig : ICarbonBlob
```

### Methods

```csharp
public Byte reserved1;
```

```csharp
public Byte reserved2;
```

```csharp
public Byte reserved3;
```

```csharp
public Byte version;
```

```csharp
public UInt32 allowedTxTypes;
```

```csharp
public UInt32 blockRateTarget;
```

```csharp
public UInt32 expiryWindow;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.GasConfig

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/GasConfig.cs`

### Declarations

```csharp
public struct GasConfig : ICarbonBlob
```

### Methods

```csharp
public Byte feeShift;
```

```csharp
public Byte gasBurnRatioShift;
```

```csharp
public Byte maxNameLength;
```

```csharp
public Byte maxTokenSymbolLength;
```

```csharp
public Byte version;
```

```csharp
public UInt32 maxStructureSize;
```

```csharp
public UInt64 dataEscrowPerRow;
```

```csharp
public UInt64 dataTokenId;
```

```csharp
public UInt64 feeMultiplier;
```

```csharp
public UInt64 gasBurnRatioMul;
```

```csharp
public UInt64 gasFeeCreateTokenBase;
```

```csharp
public UInt64 gasFeeCreateTokenSeries;
```

```csharp
public UInt64 gasFeeCreateTokenSymbol;
```

```csharp
public UInt64 gasFeePerByte;
```

```csharp
public UInt64 gasFeeQuery;
```

```csharp
public UInt64 gasFeeRegisterName;
```

```csharp
public UInt64 gasFeeTransfer;
```

```csharp
public UInt64 gasTokenId;
```

```csharp
public UInt64 minimumGasOffer;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.MarketSellTokenArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/MarketCallArgs.cs`

### Declarations

```csharp
public struct MarketSellTokenArgs : ICarbonBlob
```

### Methods

```csharp
public Bytes32 from;
```

```csharp
public Int64 endDate;
```

```csharp
public IntX price;
```

```csharp
public UInt64 instanceId;
```

```csharp
public UInt64 quoteTokenId;
```

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.MarketSellTokenByIdArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/MarketCallArgs.cs`

### Declarations

```csharp
public struct MarketSellTokenByIdArgs : ICarbonBlob
```

### Methods

```csharp
public Bytes32 from;
```

```csharp
public Int64 endDate;
```

```csharp
public IntX price;
```

```csharp
public SmallString quoteSymbol;
```

```csharp
public SmallString symbol;
```

```csharp
public VmDynamicVariable instanceId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.MarketCancelSaleArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/MarketCallArgs.cs`

### Declarations

```csharp
public struct MarketCancelSaleArgs : ICarbonBlob
```

### Methods

```csharp
public UInt64 instanceId;
```

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.MarketCancelSaleByIdArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/MarketCallArgs.cs`

### Declarations

```csharp
public struct MarketCancelSaleByIdArgs : ICarbonBlob
```

### Methods

```csharp
public SmallString symbol;
```

```csharp
public VmDynamicVariable instanceId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.MarketBuyTokenArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/MarketCallArgs.cs`

### Declarations

```csharp
public struct MarketBuyTokenArgs : ICarbonBlob
```

### Methods

```csharp
public Bytes32 from;
```

```csharp
public UInt64 instanceId;
```

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.MarketBuyTokenByIdArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/MarketCallArgs.cs`

### Declarations

```csharp
public struct MarketBuyTokenByIdArgs : ICarbonBlob
```

### Methods

```csharp
public Bytes32 from;
```

```csharp
public SmallString symbol;
```

```csharp
public VmDynamicVariable instanceId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.MarketGetTokenListingCountArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/MarketCallArgs.cs`

### Declarations

```csharp
public struct MarketGetTokenListingCountArgs : ICarbonBlob
```

### Methods

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.MarketGetTokenListingInfoArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/MarketCallArgs.cs`

### Declarations

```csharp
public struct MarketGetTokenListingInfoArgs : ICarbonBlob
```

### Methods

```csharp
public UInt64 instanceId;
```

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.MarketGetTokenListingInfoByIdArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/MarketCallArgs.cs`

### Declarations

```csharp
public struct MarketGetTokenListingInfoByIdArgs : ICarbonBlob
```

### Methods

```csharp
public SmallString symbol;
```

```csharp
public VmDynamicVariable instanceId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.MarketConfigFlags

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/MarketConfig.cs`

### Declarations

```csharp
public enum MarketConfigFlags : uint
```

### Variants

- `CanCancelEarly = 1u << 2`
- `CanPurchaseLate = 1u << 3`
- `EnforceRoyalties = 1u << 1`
- `None = 0`
- `PriceRequired = 1u << 0`

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.MarketConfigDefaults

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/MarketConfig.cs`

### Declarations

```csharp
public static class MarketConfigDefaults
```

### Methods

```csharp
public const MarketConfigFlags Flags = MarketConfigFlags.PriceRequired | MarketConfigFlags.EnforceRoyalties;
```

```csharp
public const ulong DelistingGraceMs = 1000UL * 60 * 60 * 24;
```

```csharp
public const ulong MaximumListingTimeMs = 1000UL * 60 * 60 * 24 * 90;
```

```csharp
public const ulong MinimumListingTimeMs = 1000UL;
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.MarketRoyalties

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/MarketConfig.cs`

### Declarations

```csharp
public static class MarketRoyalties
```

### Methods

```csharp
public const ulong HundredPercent = 100UL * OnePercent;
```

```csharp
public const ulong OnePercent = 10000000UL;
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.MarketConfig

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/MarketConfig.cs`

### Declarations

```csharp
public struct MarketConfig : ICarbonBlob
```

### Methods

```csharp
public MarketConfigFlags flags;
```

```csharp
public const int SerializedSize = 28;
```

```csharp
public ulong delistingGrace;
```

```csharp
public ulong maximumListingTime;
```

```csharp
public ulong minimumListingTime;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.SeriesInfo

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/SeriesInfo.cs`

### Declarations

```csharp
public struct SeriesInfo : ICarbonBlob
```

### Methods

```csharp
public Bytes32 owner;
```

```csharp
public VmStructSchema ram;
```

```csharp
public VmStructSchema rom;
```

```csharp
public byte[] metadata; // TokenInfo.tokenSchemas.seriesMetadata
```

```csharp
public uint maxMint;
```

```csharp
public uint maxSupply;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.NftMintInfo

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenCallArgs.cs`

### Declarations

```csharp
public struct NftMintInfo : ICarbonBlob
```

### Methods

```csharp
public UInt32 seriesId;
```

```csharp
public byte[] ram;
```

```csharp
public byte[] rom;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.MintNonFungibleArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenCallArgs.cs`

### Declarations

```csharp
public struct MintNonFungibleArgs : ICarbonBlob
```

### Methods

```csharp
public Bytes32 address;
```

```csharp
public NftMintInfo[] tokens;
```

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.CreateTokenSeriesArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenCallArgs.cs`

### Declarations

```csharp
public struct CreateTokenSeriesArgs : ICarbonBlob
```

### Methods

```csharp
public SeriesInfo info;
```

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.CreateMintedTokenSeriesArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenCallArgs.cs`

### Declarations

```csharp
public struct CreateMintedTokenSeriesArgs : ICarbonBlob
```

### Methods

```csharp
public Bytes32 address;
```

```csharp
public SeriesInfo info;
```

```csharp
public UInt64 tokenId;
```

```csharp
public byte[][] rams;
```

```csharp
public byte[][] roms;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.PhantasmaNftMintInfo

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenCallArgs.cs`

### Declarations

```csharp
public struct PhantasmaNftMintInfo : ICarbonBlob
```

### Methods

```csharp
public IntX phantasmaSeriesId;
```

```csharp
public byte[] ram;
```

```csharp
public byte[] rom; // public schema-driven NFT payload; chain-owned `_i` / nested `rom` are not caller input here
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.MintPhantasmaNonFungibleArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenCallArgs.cs`

### Declarations

```csharp
public struct MintPhantasmaNonFungibleArgs : ICarbonBlob
```

### Methods

```csharp
public Bytes32 address;
```

```csharp
public PhantasmaNftMintInfo[] tokens;
```

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.PhantasmaNftMintResult

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenCallArgs.cs`

### Declarations

```csharp
public struct PhantasmaNftMintResult : ICarbonBlob
```

### Methods

```csharp
public Bytes32 phantasmaNftId;
```

```csharp
public UInt64 carbonInstanceId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.MintFungibleArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenCallArgs.cs`

### Declarations

```csharp
public struct MintFungibleArgs : ICarbonBlob
```

### Methods

```csharp
public Bytes32 to;
```

```csharp
public IntX amount;
```

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.TransferFungibleArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenCallArgs.cs`

### Declarations

```csharp
public struct TransferFungibleArgs : ICarbonBlob
```

### Methods

```csharp
public Bytes32 from;
```

```csharp
public Bytes32 to;
```

```csharp
public IntX amount;
```

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.TransferNonFungibleArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenCallArgs.cs`

### Declarations

```csharp
public struct TransferNonFungibleArgs : ICarbonBlob
```

### Methods

```csharp
public Bytes32 from;
```

```csharp
public Bytes32 to;
```

```csharp
public UInt64 tokenId;
```

```csharp
public UInt64[] instanceIds;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.BurnFungibleArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenCallArgs.cs`

### Declarations

```csharp
public struct BurnFungibleArgs : ICarbonBlob
```

### Methods

```csharp
public Bytes32 from;
```

```csharp
public IntX amount;
```

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.BurnNonFungibleArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenCallArgs.cs`

### Declarations

```csharp
public struct BurnNonFungibleArgs : ICarbonBlob
```

### Methods

```csharp
public Bytes32 from;
```

```csharp
public UInt64 tokenId;
```

```csharp
public UInt64[] instanceIds;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.UpdateTokenMetadataArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenCallArgs.cs`

### Declarations

```csharp
public struct UpdateTokenMetadataArgs : ICarbonBlob
```

### Methods

```csharp
public UInt64 tokenId;
```

```csharp
public VmDynamicStruct metadata;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.UpdateSeriesMetadataArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenCallArgs.cs`

### Declarations

```csharp
public struct UpdateSeriesMetadataArgs : ICarbonBlob
```

### Methods

```csharp
public UInt32 seriesId;
```

```csharp
public UInt64 tokenId;
```

```csharp
public byte[] metadata;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.SystemAddress

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenHelper.cs`

### Declarations

```csharp
public static class SystemAddress
```

### Methods

```csharp
public static Bytes32 DataPool = Create(2);
```

```csharp
public static Bytes32 GasPool = Create(1);
```

```csharp
public static Bytes32 Null = Create(0); // All elements default to 0
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.TokenHelper

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenHelper.cs`

### Declarations

```csharp
public static class TokenHelper
```

### Methods

```csharp
public static Bytes32 GetNftAddress(UInt64 tokenId, UInt64 instanceId)
```

```csharp
public static void UnpackNftInstanceId(UInt64 instanceId, out uint seriesId, out uint mintNumber)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.TokenInfo

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenInfo.cs`

### Declarations

```csharp
public struct TokenInfo : ICarbonBlob
```

### Methods

```csharp
public Bytes32 owner;
```

```csharp
public IntX maxSupply;
```

```csharp
public SmallString symbol;
```

```csharp
public TokenFlags flags;
```

```csharp
public byte[] metadata;
```

```csharp
public byte[] tokenSchemas;
```

```csharp
public uint decimals;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.ListingType

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenListing.cs`

### Declarations

```csharp
public enum ListingType : byte
```

### Variants

- `FixedPrice`

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.TokenListing

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenListing.cs`

### Declarations

```csharp
public struct TokenListing : ICarbonBlob
```

### Methods

```csharp
public Bytes32 seller;
```

```csharp
public Int64 endDate;
```

```csharp
public Int64 startDate;
```

```csharp
public IntX price;
```

```csharp
public ListingType type;
```

```csharp
public UInt64 quoteTokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.TokenSchemas

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokenSchemas.cs`

### Declarations

```csharp
public struct TokenSchemas : ICarbonBlob
```

### Methods

```csharp
public VmStructSchema ram;
```

```csharp
public VmStructSchema rom;
```

```csharp
public VmStructSchema seriesMetadata;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Modules.TokensConfig

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Modules/TokensConfig.cs`

### Declarations

```csharp
public struct TokensConfig : ICarbonBlob
```

### Methods

```csharp
public TokensConfigFlags flags;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.SignedTxMsg

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/SignedTxMsg.cs`

### Declarations

```csharp
public struct SignedTxMsg : ICarbonBlob
```

### Methods

```csharp
public TxMsg msg;
```

```csharp
public Witness[] witnesses;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsg

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsg.cs`

### Declarations

```csharp
public struct TxMsg : ICarbonBlob
```

### Methods

```csharp
public Bytes32 gasFrom;
```

```csharp
public Int64 expiry;
```

```csharp
public SmallString payload;
```

```csharp
public TxTypes type;
```

```csharp
public UInt64 maxData;
```

```csharp
public UInt64 maxGas;
```

```csharp
public object msg;
```

```csharp
public static TxMsg FromPhantasmaRaw(byte[] rawTransaction)
```

```csharp
public static object? ReadDataByType(BinaryReader r, TxTypes type)
```

```csharp
public static void WriteDataByType(BinaryWriter w, TxTypes type, object msg)
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsgBurnFungible

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgBurnFungible.cs`

### Declarations

```csharp
public struct TxMsgBurnFungible : ICarbonBlob
```

### Methods

```csharp
public IntX amount;
```

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsgBurnFungible_GasPayer

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgBurnFungible_GasPayer.cs`

### Declarations

```csharp
public struct TxMsgBurnFungible_GasPayer : ICarbonBlob
```

### Methods

```csharp
public Bytes32 from;
```

```csharp
public IntX amount;
```

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsgBurnNonFungible

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgBurnNonFungible.cs`

### Declarations

```csharp
public struct TxMsgBurnNonFungible : ICarbonBlob
```

### Methods

```csharp
public UInt64 instanceId;
```

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsgBurnNonFungible_GasPayer

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgBurnNonFungible_GasPayer.cs`

### Declarations

```csharp
public struct TxMsgBurnNonFungible_GasPayer : ICarbonBlob
```

### Methods

```csharp
public Bytes32 from;
```

```csharp
public UInt64 instanceId;
```

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsgCall

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgCall.cs`

### Declarations

```csharp
public struct TxMsgCall : ICarbonBlob
```

### Methods

```csharp
public MsgCallArgSections sections;
```

```csharp
public UInt32 methodId;
```

```csharp
public UInt32 moduleId;
```

```csharp
public byte[] args;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.MsgCallArgs

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgCallArgSections.cs`

### Declarations

```csharp
public struct MsgCallArgs : ICarbonBlob
```

### Methods

```csharp
public byte[] args;
```

```csharp
public int registerOffset;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.MsgCallArgSections

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgCallArgSections.cs`

### Declarations

```csharp
public struct MsgCallArgSections : ICarbonBlob
```

### Methods

```csharp
public MsgCallArgs[] argSections;
```

```csharp
public bool HasSections => argSections != null && argSections.Length > 0;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void ReadWithNegativeCount(BinaryReader r, int countNegative)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsgCall_Multi

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgCall_Multi.cs`

### Declarations

```csharp
public struct TxMsgCall_Multi : ICarbonBlob
```

### Methods

```csharp
public TxMsgCall[] calls;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsgMintFungible

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgMintFungible.cs`

### Declarations

```csharp
public struct TxMsgMintFungible : ICarbonBlob
```

### Methods

```csharp
public Bytes32 to;
```

```csharp
public IntX amount;
```

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsgMintNonFungible

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgMintNonFungible.cs`

### Declarations

```csharp
public struct TxMsgMintNonFungible : ICarbonBlob
```

### Methods

```csharp
public Bytes32 to;
```

```csharp
public UInt32 seriesId;
```

```csharp
public UInt64 tokenId;
```

```csharp
public byte[] ram;
```

```csharp
public byte[] rom;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsgPhantasma

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgPhantasma.cs`

### Declarations

```csharp
public struct TxMsgPhantasma : ICarbonBlob
```

### Methods

```csharp
public SmallString chain;
```

```csharp
public SmallString nexus;
```

```csharp
public byte[] script;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsgPhantasma_Raw

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgPhantasma_Raw.cs`

### Declarations

```csharp
public struct TxMsgPhantasma_Raw : ICarbonBlob
```

### Methods

```csharp
public byte[] transaction;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsgSpecialResolution

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgSpecialResolution.cs`

### Declarations

```csharp
public struct TxMsgSpecialResolution : ICarbonBlob
```

### Methods

```csharp
public TxMsgCall[] calls;
```

```csharp
public UInt64 resolutionId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsgTrade

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgTrade.cs`

### Declarations

```csharp
public struct TxMsgTrade : ICarbonBlob
```

### Methods

```csharp
public TxMsgBurnFungible_GasPayer[] burnF;
```

```csharp
public TxMsgBurnNonFungible_GasPayer[] burnN;
```

```csharp
public TxMsgMintFungible[] mintF;
```

```csharp
public TxMsgMintNonFungible[] mintN;
```

```csharp
public TxMsgTransferFungible_GasPayer[] transferF;
```

```csharp
public TxMsgTransferNonFungible_Single_GasPayer[] transferN;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsgTransferFungible

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgTransferFungible.cs`

### Declarations

```csharp
public struct TxMsgTransferFungible : ICarbonBlob
```

### Methods

```csharp
public Bytes32 to;
```

```csharp
public UInt64 amount;
```

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsgTransferFungible_GasPayer

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgTransferFungible_GasPayer.cs`

### Declarations

```csharp
public struct TxMsgTransferFungible_GasPayer : ICarbonBlob
```

### Methods

```csharp
public Bytes32 from;
```

```csharp
public Bytes32 to;
```

```csharp
public UInt64 amount;
```

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsgTransferNonFungible_Multi

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgTransferNonFungible_Multi.cs`

### Declarations

```csharp
public struct TxMsgTransferNonFungible_Multi : ICarbonBlob
```

### Methods

```csharp
public Bytes32 to;
```

```csharp
public UInt64 tokenId;
```

```csharp
public UInt64[] instanceIds;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsgTransferNonFungible_Multi_GasPayer

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgTransferNonFungible_Multi_GasPayer.cs`

### Declarations

```csharp
public struct TxMsgTransferNonFungible_Multi_GasPayer : ICarbonBlob
```

### Methods

```csharp
public Bytes32 from;
```

```csharp
public Bytes32 to;
```

```csharp
public UInt64 tokenId;
```

```csharp
public UInt64[] instanceIds;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsgTransferNonFungible_Single

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgTransferNonFungible_Single.cs`

### Declarations

```csharp
public struct TxMsgTransferNonFungible_Single : ICarbonBlob
```

### Methods

```csharp
public Bytes32 to;
```

```csharp
public UInt64 instanceId;
```

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.TxMsgTransferNonFungible_Single_GasPayer

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/TxMsgTransferNonFungible_Single_GasPayer.cs`

### Declarations

```csharp
public struct TxMsgTransferNonFungible_Single_GasPayer : ICarbonBlob
```

### Methods

```csharp
public Bytes32 from;
```

```csharp
public Bytes32 to;
```

```csharp
public UInt64 instanceId;
```

```csharp
public UInt64 tokenId;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Vm.StandardMeta

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Vm/StandardMeta.cs`

### Declarations

```csharp
public static class StandardMeta
```

### Methods

```csharp
public static SmallString address = new("_a");
```

```csharp
public static SmallString id = new("_i");
```

```csharp
public static SmallString name = new("_n");
```

```csharp
public static SmallString nexus = new("_x");
```

```csharp
public static SmallString phantasmaRom = new("rom");
```

```csharp
public static SmallString phantasma_abi = new("_phb");
```

```csharp
public static SmallString phantasma_script = new("_phs");
```

```csharp
public static SmallString pre_burn = new("_brn");
```

```csharp
public static SmallString royalties = new("royalties");
```

```csharp
public static SmallString staking_booster_div = new("_sbd");
```

```csharp
public static SmallString staking_booster_limit = new("_sbl");
```

```csharp
public static SmallString staking_booster_mul = new("_sbm");
```

```csharp
public static SmallString staking_booster_token = new("_sbt");
```

```csharp
public static SmallString staking_lock = new("_sl");
```

```csharp
public static SmallString staking_org_id = new("_soi");
```

```csharp
public static SmallString staking_org_threshold = new("_sot");
```

```csharp
public static SmallString staking_reward_div = new("_srd");
```

```csharp
public static SmallString staking_reward_mul = new("_srm");
```

```csharp
public static SmallString staking_reward_period = new("_srp");
```

```csharp
public static SmallString staking_reward_token = new("_srt");
```

```csharp
public static SmallString tokenomics = new("_t");
```

```csharp
public static class Chain
```

```csharp
public static class Nft
```

```csharp
public static class Token
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Vm.VmDynamicStruct

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Vm/VmDynamicStruct.cs`

### Declarations

```csharp
public struct VmDynamicStruct : ICarbonBlob
```

### Methods

```csharp
public VmDynamicVariable? GetValue(SmallString key)
```

```csharp
public VmDynamicVariable? this[SmallString key]
```

```csharp
public VmDynamicVariable? this[string key]
```

```csharp
public VmNamedDynamicVariable[] fields;//NOTE: fields *must* be sorted by name
```

```csharp
public bool Write(VmStructSchema schema, BinaryWriter w)
```

```csharp
public static VmDynamicStruct New(VmStructSchema schema, byte[] bytes)
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Read(VmStructSchema schema, BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Vm.VmDynamicVariable

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Vm/VmDynamicVariable.cs`

### Declarations

```csharp
public struct VmDynamicVariable : ICarbonBlob
```

### Methods

```csharp
public BigInteger GetInt256(string e = "not Int256") { VmExpect(type == VmType.Int256, e); VmAssert(data != null, "bad variable"); return (BigInteger)data!; }
```

```csharp
public BigInteger GetUInt256(string e = "not Int256")
```

```csharp
public Int16 GetInt16(string e = "not Int16") { VmExpect(type == VmType.Int16, e); VmAssert(data != null, "bad variable"); return (Int16)data!; }
```

```csharp
public Int32 GetInt32(string e = "not Int32") { VmExpect(type == VmType.Int32, e); VmAssert(data != null, "bad variable"); return (Int32)data!; }
```

```csharp
public Int64 GetInt64(string e = "not Int64") { VmExpect(type == VmType.Int64, e); VmAssert(data != null, "bad variable"); return (Int64)data!; }
```

```csharp
public UInt16 GetUInt16(string e = "not Int16") { VmExpect(type == VmType.Int16, e); VmAssert(data != null, "bad variable"); return (UInt16)(Int16)data!; }
```

```csharp
public UInt32 GetUInt32(string e = "not Int32") { VmExpect(type == VmType.Int32, e); VmAssert(data != null, "bad variable"); return (UInt32)(Int32)data!; }
```

```csharp
public UInt64 GetUInt64(string e = "not Int64") { VmExpect(type == VmType.Int64, e); VmAssert(data != null, "bad variable"); return (UInt64)(Int64)data!; }
```

```csharp
public VmDynamicVariable() { type = VmType.Dynamic; data = null; }
```

```csharp
public VmDynamicVariable(BigInteger i) { type = VmType.Int256; data = i; }
```

```csharp
public VmDynamicVariable(Bytes16 b) { type = VmType.Bytes16; data = b; }
```

```csharp
public VmDynamicVariable(Bytes32 b) { type = VmType.Bytes32; data = b; }
```

```csharp
public VmDynamicVariable(Bytes64 b) { type = VmType.Bytes64; data = b; }
```

```csharp
public VmDynamicVariable(Int16 i) { type = VmType.Int16; data = i; }
```

```csharp
public VmDynamicVariable(Int32 i) { type = VmType.Int32; data = i; }
```

```csharp
public VmDynamicVariable(Int64 i) { type = VmType.Int64; data = i; }
```

```csharp
public VmDynamicVariable(UInt16 i) { type = VmType.Int16; data = (Int16)i; }
```

```csharp
public VmDynamicVariable(UInt32 i) { type = VmType.Int32; data = (Int32)i; }
```

```csharp
public VmDynamicVariable(UInt64 i) { type = VmType.Int64; data = (Int64)i; }
```

```csharp
public VmDynamicVariable(VmStructArray s) { type = VmType.Array | VmType.Struct; data = s; }
```

```csharp
public VmDynamicVariable(VmType t)
```

```csharp
public VmDynamicVariable(byte i) { type = VmType.Int8; data = i; }
```

```csharp
public VmDynamicVariable(byte[] b) { type = VmType.Bytes; data = b; }
```

```csharp
public VmDynamicVariable(sbyte i) { type = VmType.Int8; data = (byte)i; }
```

```csharp
public VmDynamicVariable(string s) { type = VmType.String; data = s; }
```

```csharp
public VmType type;
```

```csharp
public bool Write(VmVariableSchema schema, BinaryWriter w)
```

```csharp
public byte GetUInt8(string e = "not Int8") { VmExpect(type == VmType.Int8, e); VmAssert(data != null, "bad variable"); return (byte)data!; }
```

```csharp
public byte[] GetBytes(string e = "not Bytes") { VmExpect(type == VmType.Bytes, e); VmAssert(data != null, "bad variable"); return (byte[])data!; }
```

```csharp
public object? data;
```

```csharp
public sbyte GetInt8(string e = "not Int8") { VmExpect(type == VmType.Int8, e); VmAssert(data != null, "bad variable"); return (sbyte)(byte)data!; }
```

```csharp
public static bool Write(VmType type, VmDynamicVariable v, VmStructSchema? schema, BinaryWriter w)
```

```csharp
public static void Read(VmType type, out VmDynamicVariable v, VmStructSchema? schema, BinaryReader r)
```

```csharp
public string GetString(string e = "not String") { VmExpect(type == VmType.String, e); VmAssert(data != null, "bad variable"); return (string)data!; }
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Read(VmVariableSchema schema, BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Vm.VmNamedDynamicVariable

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Vm/VmNamedDynamicVariable.cs`

### Declarations

```csharp
public struct VmNamedDynamicVariable : ICarbonBlob
```

### Methods

```csharp
public SmallString name;
```

```csharp
public VmDynamicVariable value;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Vm.VmNamedVariableSchema

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Vm/VmNamedVariableSchema.cs`

### Declarations

```csharp
public struct VmNamedVariableSchema : ICarbonBlob
```

### Methods

```csharp
public SmallString name;
```

```csharp
public VmVariableSchema schema;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Vm.VmStructArray

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Vm/VmStructArray.cs`

### Declarations

```csharp
public class VmStructArray
```

### Methods

```csharp
public VmDynamicStruct[] structs = Array.Empty<VmDynamicStruct>();
```

```csharp
public VmStructSchema schema = new VmStructSchema { fields = Array.Empty<VmNamedVariableSchema>(), flags = VmStructSchema.Flags.None };
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Vm.VmStructSchema

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Vm/VmStructSchema.cs`

### Declarations

```csharp
public struct VmStructSchema : ICarbonBlob
```

### Methods

```csharp
public Flags flags;
```

```csharp
public VmNamedVariableSchema[] fields;
```

```csharp
public enum Flags
```

```csharp
public static VmStructSchema CreateEmpty()
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Blockchain.Vm.VmVariableSchema

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Blockchain/Vm/VmVariableSchema.cs`

### Declarations

```csharp
public struct VmVariableSchema : ICarbonBlob
```

### Methods

```csharp
public VmStructSchema structure;
```

```csharp
public VmType type;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Bytes16

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Bytes16.cs`

### Declarations

```csharp
public struct Bytes16 : ICarbonBlob
```

### Methods

```csharp
public Bytes16()
```

```csharp
public Bytes16(byte[] data)
```

```csharp
public bool Equals(Bytes16 obj)
```

```csharp
public byte[] bytes;
```

```csharp
public override bool Equals(object? obj)
```

```csharp
public override int GetHashCode()
```

```csharp
public readonly static Bytes16 Empty = new();
```

```csharp
public static explicit operator byte[](Bytes16 v)
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Bytes32

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Bytes32.cs`

### Declarations

```csharp
public struct Bytes32 : ICarbonBlob
```

### Methods

```csharp
public Bytes32()
```

```csharp
public Bytes32(byte[] data)
```

```csharp
public Bytes32(byte[] data, int offset)
```

```csharp
public Bytes32(string hex) : this(hex.FromHex() ?? Array.Empty<byte>())
```

```csharp
public bool Equals(Bytes32 obj)
```

```csharp
public byte[] bytes;
```

```csharp
public override bool Equals(object? obj)
```

```csharp
public override int GetHashCode()
```

```csharp
public readonly static Bytes32 Empty = new();
```

```csharp
public static explicit operator byte[](Bytes32 v)
```

```csharp
public string ToHex()
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Bytes64

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Bytes64.cs`

### Declarations

```csharp
public struct Bytes64 : ICarbonBlob
```

### Methods

```csharp
public Bytes64()
```

```csharp
public Bytes64(byte[] data)
```

```csharp
public bool Equals(Bytes64 obj)
```

```csharp
public byte[] bytes;
```

```csharp
public override bool Equals(object? obj)
```

```csharp
public override int GetHashCode()
```

```csharp
public readonly static Bytes64 Empty = new();
```

```csharp
public static explicit operator byte[](Bytes64 v)
```

```csharp
public string ToHex()
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.CarbonBlob

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/CarbonBlob.cs`

### Declarations

```csharp
public static class CarbonBlob
```

### Methods

```csharp
public static T New<T>(BinaryReader r) where T : ICarbonBlob, new()
```

```csharp
public static T New<T>(Stream s, bool allowTrailingBytes = false) where T : ICarbonBlob, new()
```

```csharp
public static T New<T>(byte[] bytes, bool allowTrailingBytes = false, long offset = 0) where T : ICarbonBlob, new()
```

```csharp
public static T New<T>(byte[] bytes, long offset) where T : ICarbonBlob, new()
```

```csharp
public static byte[] Serialize<T>(T carbonBlob) where T : ICarbonBlob, new()
```

## PhantasmaPhoenix.Protocol.Carbon.IntX

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/IntX.cs`

### Declarations

```csharp
public struct IntX : ICarbonBlob
```

### Methods

```csharp
public IntX(BigInteger v)
```

```csharp
public IntX(Int64 v)
```

```csharp
public bool IsZero
```

```csharp
public override string ToString()
```

```csharp
public static IntX operator -(IntX a)
```

```csharp
public static IntX operator -(IntX a, IntX b)
```

```csharp
public static explicit operator BigInteger(IntX self)
```

```csharp
public static explicit operator Int64(IntX self)
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.SmallString

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/SmallString.cs`

### Declarations

```csharp
public struct SmallString : ICarbonBlob
```

### Methods

```csharp
public SmallString() { data = ""; }
```

```csharp
public SmallString(string s)
```

```csharp
public byte[] GetBytes()
```

```csharp
public int CompareTo(SmallString other) { return data.CompareTo(other.data); }
```

```csharp
public readonly static SmallString Empty = new SmallString { data = "" };
```

```csharp
public static SmallString FromBytes(byte[] bytes)
```

```csharp
public static SmallString FromBytes(byte[] bytes, int index, int count)
```

```csharp
public string data;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.Protocol.Carbon.Witness

Source: `PhantasmaPhoenix.Protocol.Carbon/src/Structures/Witness.cs`

### Declarations

```csharp
public struct Witness : ICarbonBlob
```

### Methods

```csharp
public Bytes32 address;
```

```csharp
public Bytes64 signature;
```

```csharp
public void Read(BinaryReader r)
```

```csharp
public void Write(BinaryWriter w)
```

## PhantasmaPhoenix.RPC.Annotations.ApiDescriptionAttribute

Source: `PhantasmaPhoenix.RPC/src/Annotations/ApiAttributes.cs`

### Declarations

```csharp
public class ApiDescriptionAttribute : Attribute
```

### Methods

```csharp
public ApiDescriptionAttribute(string description)
```

```csharp
public readonly string Description;
```

## PhantasmaPhoenix.RPC.Annotations.ApiParameterAttribute

Source: `PhantasmaPhoenix.RPC/src/Annotations/ApiAttributes.cs`

### Declarations

```csharp
public class ApiParameterAttribute : ApiDescriptionAttribute
```

### Methods

```csharp
public ApiParameterAttribute(string description) : base(description)
```

```csharp
public ApiParameterAttribute(string description, string value) : base(description)
```

```csharp
public bool? Required { get; set; }
```

```csharp
public readonly string? Value;
```

## PhantasmaPhoenix.RPC.Annotations.ApiInfoAttribute

Source: `PhantasmaPhoenix.RPC/src/Annotations/ApiAttributes.cs`

### Declarations

```csharp
public class ApiInfoAttribute : ApiDescriptionAttribute
```

### Methods

```csharp
public ApiInfoAttribute(Type returnType, string description, bool paginated = false, int cacheDuration = 0, string? cacheTag = null) : base(description)
```

```csharp
public readonly Type ReturnType;
```

```csharp
public readonly bool Paginated;
```

```csharp
public readonly int CacheDuration;
```

```csharp
public readonly string? CacheTag;
```

## PhantasmaPhoenix.RPC.Models.ABIEventResult

Source: `PhantasmaPhoenix.RPC/src/Models/ABIEventResult.cs`

### Declarations

```csharp
public class ABIEventResult
```

### Methods

```csharp
public ABIEventResult() { }
```

```csharp
public int Value { get; set; }
```

```csharp
public string Description { get; set; }
```

```csharp
public string Name { get; set; }
```

```csharp
public string ReturnType { get; set; }
```

## PhantasmaPhoenix.RPC.Models.ABIMethodResult

Source: `PhantasmaPhoenix.RPC/src/Models/ABIMethodResult.cs`

### Declarations

```csharp
public class ABIMethodResult
```

### Methods

```csharp
public ABIMethodResult() { }
```

```csharp
public ABIParameterResult[] Parameters { get; set; }
```

```csharp
public string Name { get; set; }
```

```csharp
public string ReturnType { get; set; }
```

## PhantasmaPhoenix.RPC.Models.ABIParameterResult

Source: `PhantasmaPhoenix.RPC/src/Models/ABIParameterResult.cs`

### Declarations

```csharp
public class ABIParameterResult
```

### Methods

```csharp
public ABIParameterResult() { }
```

```csharp
public string Name { get; set; }
```

```csharp
public string Type { get; set; }
```

## PhantasmaPhoenix.RPC.Models.AccountResult

Source: `PhantasmaPhoenix.RPC/src/Models/AccountResult.cs`

### Declarations

```csharp
public class AccountResult
```

### Methods

```csharp
public AccountResult() { }
```

```csharp
public BalanceResult[] Balances { get; set; }
```

```csharp
public StakeResult Stakes { get; set; }
```

```csharp
public StorageResult Storage { get; set; }
```

```csharp
public string Address { get; set; }
```

```csharp
public string Name { get; set; }
```

```csharp
public string Relay { get; set; }
```

```csharp
public string Stake { get; set; } //Deprecated
```

```csharp
public string Unclaimed { get; set; } //Deprecated
```

```csharp
public string Validator { get; set; }
```

```csharp
public string[] Txs { get; set; }
```

## PhantasmaPhoenix.RPC.Models.AccountTransactionsResult

Source: `PhantasmaPhoenix.RPC/src/Models/AccountTransactionsResult.cs`

### Declarations

```csharp
public class AccountTransactionsResult
```

### Methods

```csharp
public AccountTransactionsResult() { }
```

```csharp
public TransactionResult[] Txs { get; set; }
```

```csharp
public string Address { get; set; }
```

## PhantasmaPhoenix.RPC.Models.ArchiveResult

Source: `PhantasmaPhoenix.RPC/src/Models/ArchiveResult.cs`

### Declarations

```csharp
public class ArchiveResult
```

### Methods

```csharp
public ArchiveResult() { }
```

```csharp
public int BlockCount { get; set; }
```

```csharp
public int[] MissingBlocks { get; set; }
```

```csharp
public string Encryption { get; set; }
```

```csharp
public string Hash { get; set; }
```

```csharp
public string Name { get; set; }
```

```csharp
public string[] Owners { get; set; }
```

```csharp
public uint Size { get; set; }
```

```csharp
public uint Time { get; set; }
```

## PhantasmaPhoenix.RPC.Models.AuctionResult

Source: `PhantasmaPhoenix.RPC/src/Models/AuctionResult.cs`

### Declarations

```csharp
public class AuctionResult
```

### Methods

```csharp
public AuctionResult() { }
```

```csharp
public string BaseSymbol { get; set; }
```

```csharp
public string ChainAddress { get; set; }
```

```csharp
public string CreatorAddress { get; set; }
```

```csharp
public string CurrentWinner { get; set; }
```

```csharp
public string EndPrice { get; set; }
```

```csharp
public string ExtensionPeriod { get; set; }
```

```csharp
public string ListingFee { get; set; }
```

```csharp
public string Price { get; set; }
```

```csharp
public string QuoteSymbol { get; set; }
```

```csharp
public string Ram { get; set; }
```

```csharp
public string Rom { get; set; }
```

```csharp
public string TokenId { get; set; }
```

```csharp
public string Type { get; set; }
```

```csharp
public uint EndDate { get; set; }
```

```csharp
public uint StartDate { get; set; }
```

## PhantasmaPhoenix.RPC.Models.BalanceResult

Source: `PhantasmaPhoenix.RPC/src/Models/BalanceResult.cs`

### Declarations

```csharp
public class BalanceResult
```

### Methods

```csharp
public BalanceResult() { }
```

```csharp
public string Amount { get; set; }
```

```csharp
public string Chain { get; set; }
```

```csharp
public string Symbol { get; set; }
```

```csharp
public string[] Ids { get; set; }
```

```csharp
public uint Decimals { get; set; }
```

## PhantasmaPhoenix.RPC.Models.BlockResult

Source: `PhantasmaPhoenix.RPC/src/Models/BlockResult.cs`

### Declarations

```csharp
public class BlockResult
```

### Methods

```csharp
public BlockResult() { }
```

```csharp
public EventResult[] Events { get; set; }
```

```csharp
public OracleResult[] Oracles { get; set; }
```

```csharp
public TransactionResult[] Txs { get; set; }
```

```csharp
public string ChainAddress { get; set; }
```

```csharp
public string Hash { get; set; }
```

```csharp
public string PreviousHash { get; set; }
```

```csharp
public string Reward { get; set; }
```

```csharp
public string ValidatorAddress { get; set; }
```

```csharp
public uint Height { get; set; }
```

```csharp
public uint Protocol { get; set; }
```

```csharp
public uint Timestamp { get; set; }
```

## PhantasmaPhoenix.RPC.Models.ChainResult

Source: `PhantasmaPhoenix.RPC/src/Models/ChainResult.cs`

### Declarations

```csharp
public class ChainResult
```

### Methods

```csharp
public ChainResult() { }
```

```csharp
public string Address { get; set; }
```

```csharp
public string Name { get; set; }
```

```csharp
public string Organization { get; set; }
```

```csharp
public string Parent { get; set; }
```

```csharp
public string[] Contracts { get; set; }
```

```csharp
public string[] Dapps { get; set; }
```

```csharp
public uint Height { get; set; }
```

## PhantasmaPhoenix.RPC.Models.ContractResult

Source: `PhantasmaPhoenix.RPC/src/Models/ContractResult.cs`

### Declarations

```csharp
public class ContractResult
```

### Methods

```csharp
public ABIEventResult[] Events { get; set; }
```

```csharp
public ABIMethodResult[] Methods { get; set; }
```

```csharp
public ContractResult() { }
```

```csharp
public string Address { get; set; }
```

```csharp
public string Name { get; set; }
```

```csharp
public string Script { get; set; }
```

## PhantasmaPhoenix.RPC.Models.EventExResult

Source: `PhantasmaPhoenix.RPC/src/Models/EventExResult.cs`

### Declarations

```csharp
public class EventExResult
```

### Methods

```csharp
public EventExResult()
```

```csharp
public EventExResult(string address, string contract, EventKind kind, object data)
```

```csharp
public EventKind Kind { get; set; }
```

```csharp
public object Data { get; set; }
```

```csharp
public string Address { get; set; }
```

```csharp
public string Contract { get; set; }
```

## PhantasmaPhoenix.RPC.Models.EventResult

Source: `PhantasmaPhoenix.RPC/src/Models/EventResult.cs`

### Declarations

```csharp
public class EventResult
```

### Methods

```csharp
public EventResult() { }
```

```csharp
public EventResult(Event e)
```

```csharp
public EventResult(string address, string contract, string kind, string name, string data)
```

```csharp
public string Address { get; set; }
```

```csharp
public string Contract { get; set; }
```

```csharp
public string Data { get; set; }
```

```csharp
public string Kind { get; set; }
```

```csharp
public string Name { get; set; }
```

## PhantasmaPhoenix.RPC.Models.GovernanceResult

Source: `PhantasmaPhoenix.RPC/src/Models/GovernanceResult.cs`

### Declarations

```csharp
public class GovernanceResult
```

### Methods

```csharp
public GovernanceResult() { }
```

```csharp
public string Name { get; set; }
```

```csharp
public string Value { get; set; }
```

## PhantasmaPhoenix.RPC.Models.LeaderboardResult

Source: `PhantasmaPhoenix.RPC/src/Models/LeaderboardResult.cs`

### Declarations

```csharp
public class LeaderboardResult
```

### Methods

```csharp
public LeaderboardResult() { }
```

```csharp
public LeaderboardRowResult[] Rows { get; set; }
```

```csharp
public string Name { get; set; }
```

## PhantasmaPhoenix.RPC.Models.LeaderboardRowResult

Source: `PhantasmaPhoenix.RPC/src/Models/LeaderboardRowResult.cs`

### Declarations

```csharp
public class LeaderboardRowResult
```

### Methods

```csharp
public LeaderboardRowResult() { }
```

```csharp
public string Address { get; set; }
```

```csharp
public string Value { get; set; }
```

## PhantasmaPhoenix.RPC.Models.NexusResult

Source: `PhantasmaPhoenix.RPC/src/Models/NexusResult.cs`

### Declarations

```csharp
public class NexusResult
```

### Methods

```csharp
public ChainResult[] Chains { get; set; }
```

```csharp
public GovernanceResult[] Governance { get; set; }
```

```csharp
public NexusResult() { }
```

```csharp
public TokenResult[] Tokens { get; set; }
```

```csharp
public string Name { get; set; }
```

```csharp
public string[] Organizations { get; set; }
```

```csharp
public uint Protocol { get; set; }
```

## PhantasmaPhoenix.RPC.Models.OracleResult

Source: `PhantasmaPhoenix.RPC/src/Models/OracleResult.cs`

### Declarations

```csharp
public class OracleResult
```

### Methods

```csharp
public OracleResult() { }
```

```csharp
public string Content { get; set; }
```

```csharp
public string Url { get; set; }
```

## PhantasmaPhoenix.RPC.Models.OrganizationResult

Source: `PhantasmaPhoenix.RPC/src/Models/OrganizationResult.cs`

### Declarations

```csharp
public class OrganizationResult
```

### Methods

```csharp
public OrganizationResult() { }
```

```csharp
public string Id { get; set; }
```

```csharp
public string Name { get; set; }
```

```csharp
public string[] Members { get; set; }
```

## PhantasmaPhoenix.RPC.Models.ScriptResult

Source: `PhantasmaPhoenix.RPC/src/Models/ScriptResult.cs`

### Declarations

```csharp
public class ScriptResult
```

### Methods

```csharp
public EventResult[] Events { get; set; }
```

```csharp
public OracleResult[] Oracles { get; set; }
```

```csharp
public ScriptResult() { }
```

```csharp
public string Error { get; set; } // deprecated
```

```csharp
public string Result { get; set; } // deprecated
```

```csharp
public string[] Results { get; set; }
```

## PhantasmaPhoenix.RPC.Models.StakeResult

Source: `PhantasmaPhoenix.RPC/src/Models/StakeResult.cs`

### Declarations

```csharp
public class StakeResult
```

### Methods

```csharp
public StakeResult() { }
```

```csharp
public string Amount { get; set; }
```

```csharp
public string Unclaimed { get; set; }
```

```csharp
public uint Time { get; set; }
```

## PhantasmaPhoenix.RPC.Models.StorageResult

Source: `PhantasmaPhoenix.RPC/src/Models/StorageResult.cs`

### Declarations

```csharp
public class StorageResult
```

### Methods

```csharp
public ArchiveResult[] Archives { get; set; }
```

```csharp
public StorageResult() { }
```

```csharp
public string Avatar { get; set; }
```

```csharp
public uint Available { get; set; }
```

```csharp
public uint Used { get; set; }
```

## PhantasmaPhoenix.RPC.Models.TokenDataResult

Source: `PhantasmaPhoenix.RPC/src/Models/TokenDataResult.cs`

### Declarations

```csharp
public class TokenDataResult
```

### Methods

```csharp
public TokenDataResult() { }
```

```csharp
public TokenPropertyResult[] Infusion { get; set; }
```

```csharp
public TokenPropertyResult[] Properties { get; set; }
```

```csharp
public TokenStatus Status { get; set; }
```

```csharp
public string ChainName { get; set; }
```

```csharp
public string CreatorAddress { get; set; }
```

```csharp
public string Id { get; set; }
```

```csharp
public string Mint { get; set; }
```

```csharp
public string OwnerAddress { get; set; }
```

```csharp
public string Ram { get; set; }
```

```csharp
public string Rom { get; set; }
```

```csharp
public string Series { get; set; }
```

```csharp
public string carbonNftAddress { get; set; }
```

```csharp
public string carbonSeriesId { get; set; }
```

```csharp
public string carbonTokenId { get; set; }
```

## PhantasmaPhoenix.RPC.Models.TokenPropertyResult

Source: `PhantasmaPhoenix.RPC/src/Models/TokenPropertyResult.cs`

### Declarations

```csharp
public class TokenPropertyResult
```

### Methods

```csharp
public TokenPropertyResult() { }
```

```csharp
public string Key { get; set; }
```

```csharp
public string Value { get; set; }
```

## PhantasmaPhoenix.RPC.Models.TokenResult

Source: `PhantasmaPhoenix.RPC/src/Models/TokenResult.cs`

### Declarations

```csharp
public class TokenResult
```

### Methods

```csharp
public TokenPropertyResult[]? Metadata { get; set; }
```

```csharp
public TokenResult() { }
```

```csharp
public TokenSchemasResult? TokenSchemas { get; set; }
```

```csharp
public TokenSeriesResult[] Series { get; set; }
```

```csharp
public bool IsBurnable()
```

```csharp
public bool IsFungible()
```

```csharp
public bool IsTransferable()
```

```csharp
public string Address { get; set; }
```

```csharp
public string BurnedSupply { get; set; }
```

```csharp
public string CarbonId { get; set; }
```

```csharp
public string CurrentSupply { get; set; }
```

```csharp
public string Flags { get; set; }
```

```csharp
public string MaxSupply { get; set; }
```

```csharp
public string Name { get; set; }
```

```csharp
public string Owner { get; set; }
```

```csharp
public string Script { get; set; }
```

```csharp
public string Symbol { get; set; }
```

```csharp
public uint Decimals { get; set; }
```

## PhantasmaPhoenix.RPC.Models.TokenSchemasResult

Source: `PhantasmaPhoenix.RPC/src/Models/TokenSchemasResult.cs`

### Declarations

```csharp
public class TokenSchemasResult
```

### Methods

```csharp
public TokenSchemasResult() { }
```

```csharp
public VmStructSchemaResult Ram { get; set; }
```

```csharp
public VmStructSchemaResult Rom { get; set; }
```

```csharp
public VmStructSchemaResult SeriesMetadata { get; set; }
```

## PhantasmaPhoenix.RPC.Models.TokenSeriesResult

Source: `PhantasmaPhoenix.RPC/src/Models/TokenSeriesResult.cs`

### Declarations

```csharp
public class TokenSeriesResult
```

### Methods

```csharp
public ABIMethodResult[] Methods { get; set; }
```

```csharp
public TokenPropertyResult[] Metadata { get; set; }
```

```csharp
public TokenSeriesResult() { }
```

```csharp
public string BurnedSupply { get; set; }
```

```csharp
public string CurrentSupply { get; set; }
```

```csharp
public string MaxMint { get; set; }
```

```csharp
public string MaxSupply { get; set; }
```

```csharp
public string MintCount { get; set; }
```

```csharp
public string Mode { get; set; }
```

```csharp
public string OwnerAddress { get; set; }
```

```csharp
public string Script { get; set; }
```

```csharp
public string SeriesId { get; set; }
```

```csharp
public string carbonSeriesId { get; set; }
```

```csharp
public string carbonTokenId { get; set; }
```

## PhantasmaPhoenix.RPC.Models.TransactionResult

Source: `PhantasmaPhoenix.RPC/src/Models/TransactionResult.cs`

### Declarations

```csharp
public class TransactionResult
```

### Methods

```csharp
public EventExResult[] ExtendedEvents { get; set; }
```

```csharp
public EventResult[] Events { get; set; }
```

```csharp
public ExecutionState State { get; set; }
```

```csharp
public TransactionResult() { }
```

```csharp
public TransactionSignatureResult[]? Signatures { get; set; }
```

```csharp
public UInt64 BlockHeight { get; set; }
```

```csharp
public UInt64 Expiration { get; set; }
```

```csharp
public UInt64 Timestamp { get; set; }
```

```csharp
public byte CarbonTxType { get; set; }
```

```csharp
public string BlockHash { get; set; }
```

```csharp
public string CarbonTxData { get; set; }
```

```csharp
public string ChainAddress { get; set; }
```

```csharp
public string Fee { get; set; }
```

```csharp
public string GasLimit { get; set; }
```

```csharp
public string GasPayer { get; set; }
```

```csharp
public string GasPrice { get; set; } = "";
```

```csharp
public string GasTarget { get; set; } = "NULL";
```

```csharp
public string Hash { get; set; }
```

```csharp
public string Payload { get; set; }
```

```csharp
public string Result { get; set; }
```

```csharp
public string Script { get; set; }
```

```csharp
public string Sender { get; set; } = Address.Null.Text; // Initialized as in original Phantasma code.
```

```csharp
public string? DebugComment { get; set; }
```

## PhantasmaPhoenix.RPC.Models.TransactionSignatureResult

Source: `PhantasmaPhoenix.RPC/src/Models/TransactionSignatureResult.cs`

### Declarations

```csharp
public class TransactionSignatureResult
```

### Methods

```csharp
public TransactionSignatureResult() { }
```

```csharp
public string Data { get; set; }
```

```csharp
public string Kind { get; set; }
```

## PhantasmaPhoenix.RPC.Models.VmNamedVariableSchemaResult

Source: `PhantasmaPhoenix.RPC/src/Models/VmNamedVariableSchemaResult.cs`

### Declarations

```csharp
public class VmNamedVariableSchemaResult
```

### Methods

```csharp
public VmNamedVariableSchemaResult() { }
```

```csharp
public VmVariableSchemaResult Schema { get; set; }
```

```csharp
public string Name { get; set; }
```

## PhantasmaPhoenix.RPC.Models.VmStructSchemaResult

Source: `PhantasmaPhoenix.RPC/src/Models/VmStructSchemaResult.cs`

### Declarations

```csharp
public class VmStructSchemaResult
```

### Methods

```csharp
public VmNamedVariableSchemaResult[] Fields { get; set; }
```

```csharp
public VmStructSchemaResult() { }
```

```csharp
public uint Flags { get; set; }
```

## PhantasmaPhoenix.RPC.Models.VmVariableSchemaResult

Source: `PhantasmaPhoenix.RPC/src/Models/VmVariableSchemaResult.cs`

### Declarations

```csharp
public class VmVariableSchemaResult
```

### Methods

```csharp
public VmStructSchemaResult Schema { get; set; }
```

```csharp
public VmType Type { get; set; }
```

```csharp
public VmVariableSchemaResult() { }
```

## PhantasmaPhoenix.RPC.PhantasmaAPI

Source: `PhantasmaPhoenix.RPC/src/PhantasmaAPI.cs`

### Declarations

```csharp
public class PhantasmaAPI : IDisposable
```

### Methods

```csharp
public PhantasmaAPI(string host, RpcClient? rpcClient)
```

```csharp
public Task<AccountResult?> GetAccountAsync( string address, bool extended, bool checkAddressReservedByte, RpcAddressType addressType) => _rpc.SendRpcAsync<AccountResult>(Host, "getAccount", address, extended, checkAddressReservedByte, addressType);
```

```csharp
public Task<AccountResult?> GetAccountAsync(string address) => _rpc.SendRpcAsync<AccountResult>(Host, "getAccount", address);
```

```csharp
public Task<AccountResult[]?> GetAccountsAsync( string[] addresses, bool extended, bool checkAddressReservedByte, RpcAddressType addressType) => _rpc.SendRpcAsync<AccountResult[]>( Host, "getAccounts", string.Join(",", addresses ?? Array.Empty<string>()), extended, checkAddressReservedByte, addressType);
```

```csharp
public Task<AccountResult[]?> GetAccountsAsync(string[] addresses) => _rpc.SendRpcAsync<AccountResult[]>(Host, "getAccounts", string.Join(",", addresses ?? Array.Empty<string>()));
```

```csharp
public Task<ArchiveResult?> GetArchiveAsync(string hash) => _rpc.SendRpcAsync<ArchiveResult>(Host, "getArchive", hash);
```

```csharp
public Task<AuctionResult?> GetAuctionAsync(string chainAddressOrName, string symbol, string id) => _rpc.SendRpcAsync<AuctionResult>(Host, "getAuction", chainAddressOrName, symbol, id);
```

```csharp
public Task<BalanceResult?> GetTokenBalanceAsync( string address, string symbol, string chain, bool checkAddressReservedByte, RpcAddressType addressType) => _rpc.SendRpcAsync<BalanceResult>(Host, "getTokenBalance", address, symbol, chain, checkAddressReservedByte, addressType);
```

```csharp
public Task<BalanceResult?> GetTokenBalanceAsync(string address, string symbol, string chain = "main") => _rpc.SendRpcAsync<BalanceResult>(Host, "getTokenBalance", address, symbol, chain);
```

```csharp
public Task<BlockResult?> GetBlockByHashAsync(string blockHash) => _rpc.SendRpcAsync<BlockResult>(Host, "getBlockByHash", blockHash);
```

```csharp
public Task<BlockResult?> GetBlockByHeightAsync(string chain, long height) => _rpc.SendRpcAsync<BlockResult>(Host, "getBlockByHeight", chain, height.ToString());
```

```csharp
public Task<BlockResult?> GetLatestBlockAsync(string chain) => _rpc.SendRpcAsync<BlockResult>(Host, "getLatestBlock", chain);
```

```csharp
public Task<ChainResult?> GetChainAsync(string name = "main", bool extended = true) => _rpc.SendRpcAsync<ChainResult>(Host, "getChain", name, extended);
```

```csharp
public Task<ChainResult[]?> GetChainsAsync() => _rpc.SendRpcAsync<ChainResult[]>(Host, "getChains");
```

```csharp
public Task<ContractResult?> GetContractAsync(string contractName) => _rpc.SendRpcAsync<ContractResult>(Host, "getContract", PhantasmaPhoenix.Protocol.DomainSettings.RootChainName, contractName);
```

```csharp
public Task<ContractResult?> GetContractByAddressAsync(string chainAddressOrName, string contractAddress) => _rpc.SendRpcAsync<ContractResult>(Host, "getContractByAddress", chainAddressOrName, contractAddress);
```

```csharp
public Task<ContractResult[]?> GetContractsAsync() => _rpc.SendRpcAsync<ContractResult[]>(Host, "getContracts", PhantasmaPhoenix.Protocol.DomainSettings.RootChainName);
```

```csharp
public Task<CursorPaginatedResult<BalanceResult[]>?> GetAccountFungibleTokensAsync( string account, string tokenSymbol = "", ulong carbonTokenId = 0, uint pageSize = 10, string cursor = "", bool checkAddressReservedByte = true) => _rpc.SendRpcAsync<CursorPaginatedResult<BalanceResult[]>>( Host, "getAccountFungibleTokens", account, tokenSymbol, carbonTokenId, pageSize, cursor, checkAddressReservedByte);
```

```csharp
public Task<CursorPaginatedResult<BalanceResult[]>?> GetAccountFungibleTokensAsync( string account, string tokenSymbol, ulong carbonTokenId, uint pageSize, string cursor, bool checkAddressReservedByte, RpcAddressType addressType) => _rpc.SendRpcAsync<CursorPaginatedResult<BalanceResult[]>>( Host, "getAccountFungibleTokens", account, tokenSymbol, carbonTokenId, pageSize, cursor, checkAddressReservedByte, addressType);
```

```csharp
public Task<CursorPaginatedResult<TokenDataResult[]>?> GetAccountNFTsAsync( string account, string tokenSymbol = "", ulong carbonTokenId = 0, uint carbonSeriesId = 0, uint pageSize = 10, string cursor = "", bool extended = false, bool checkAddressReservedByte = true) => _rpc.SendRpcAsync<CursorPaginatedResult<TokenDataResult[]>>( Host, "getAccountNFTs", account, tokenSymbol, carbonTokenId, carbonSeriesId, pageSize, cursor, extended, checkAddressReservedByte);
```

```csharp
public Task<CursorPaginatedResult<TokenDataResult[]>?> GetAccountNFTsAsync( string account, string tokenSymbol, ulong carbonTokenId, uint carbonSeriesId, uint pageSize, string cursor, bool extended, bool checkAddressReservedByte, RpcAddressType addressType) => _rpc.SendRpcAsync<CursorPaginatedResult<TokenDataResult[]>>( Host, "getAccountNFTs", account, tokenSymbol, carbonTokenId, carbonSeriesId, pageSize, cursor, extended, checkAddressReservedByte, addressType);
```

```csharp
public Task<CursorPaginatedResult<TokenDataResult[]>?> GetTokenNFTsAsync( ulong carbonTokenId, uint carbonSeriesId = 0, uint pageSize = 10, string cursor = "", bool extended = false, string seriesId = "") => _rpc.SendRpcAsync<CursorPaginatedResult<TokenDataResult[]>>( Host, "getTokenNFTs", carbonTokenId, carbonSeriesId, pageSize, cursor, extended, seriesId);
```

```csharp
public Task<CursorPaginatedResult<TokenResult[]>?> GetAccountOwnedTokensAsync( string account, string tokenSymbol = "", ulong carbonTokenId = 0, uint pageSize = 10, string cursor = "", bool checkAddressReservedByte = true) => _rpc.SendRpcAsync<CursorPaginatedResult<TokenResult[]>>( Host, "getAccountOwnedTokens", account, tokenSymbol, carbonTokenId, pageSize, cursor, checkAddressReservedByte);
```

```csharp
public Task<CursorPaginatedResult<TokenResult[]>?> GetAccountOwnedTokensAsync( string account, string tokenSymbol, ulong carbonTokenId, uint pageSize, string cursor, bool checkAddressReservedByte, RpcAddressType addressType) => _rpc.SendRpcAsync<CursorPaginatedResult<TokenResult[]>>( Host, "getAccountOwnedTokens", account, tokenSymbol, carbonTokenId, pageSize, cursor, checkAddressReservedByte, addressType);
```

```csharp
public Task<CursorPaginatedResult<TokenSeriesResult[]>?> GetAccountOwnedTokenSeriesAsync( string account, string tokenSymbol = "", ulong carbonTokenId = 0, uint pageSize = 10, string cursor = "", bool checkAddressReservedByte = true) => _rpc.SendRpcAsync<CursorPaginatedResult<TokenSeriesResult[]>>( Host, "getAccountOwnedTokenSeries", account, tokenSymbol, carbonTokenId, pageSize, cursor, checkAddressReservedByte);
```

```csharp
public Task<CursorPaginatedResult<TokenSeriesResult[]>?> GetAccountOwnedTokenSeriesAsync( string account, string tokenSymbol, ulong carbonTokenId, uint pageSize, string cursor, bool checkAddressReservedByte, RpcAddressType addressType) => _rpc.SendRpcAsync<CursorPaginatedResult<TokenSeriesResult[]>>( Host, "getAccountOwnedTokenSeries", account, tokenSymbol, carbonTokenId, pageSize, cursor, checkAddressReservedByte, addressType);
```

```csharp
public Task<CursorPaginatedResult<TokenSeriesResult[]>?> GetTokenSeriesAsync( string symbol = "", ulong carbonTokenId = 0, uint pageSize = 10, string cursor = "") => _rpc.SendRpcAsync<CursorPaginatedResult<TokenSeriesResult[]>>( Host, "getTokenSeries", symbol, carbonTokenId, pageSize, cursor);
```

```csharp
public Task<LeaderboardResult?> GetLeaderboardAsync(string name) => _rpc.SendRpcAsync<LeaderboardResult>(Host, "getLeaderboard", name);
```

```csharp
public Task<NexusResult?> GetNexusAsync() => _rpc.SendRpcAsync<NexusResult>(Host, "getNexus");
```

```csharp
public Task<OrganizationResult?> GetOrganizationAsync(string id) => _rpc.SendRpcAsync<OrganizationResult>(Host, "getOrganization", id);
```

```csharp
public Task<OrganizationResult?> GetOrganizationByNameAsync(string name) => _rpc.SendRpcAsync<OrganizationResult>(Host, "getOrganizationByName", name);
```

```csharp
public Task<OrganizationResult[]?> GetOrganizationsAsync() => _rpc.SendRpcAsync<OrganizationResult[]>(Host, "getOrganizations");
```

```csharp
public Task<ScriptResult?> InvokeRawScriptAsync(string chain, string scriptData) => _rpc.SendRpcAsync<ScriptResult>(Host, "invokeRawScript", chain, scriptData);
```

```csharp
public Task<TokenDataResult?> GetNFTAsync(string symbol, string tokenId, bool loadProperties) => _rpc.SendRpcAsync<TokenDataResult>(Host, "getNFT", symbol, tokenId, loadProperties);
```

```csharp
public Task<TokenDataResult?> GetTokenDataAsync(string symbol, string tokenId) => _rpc.SendRpcAsync<TokenDataResult>(Host, "getTokenData", symbol, tokenId);
```

```csharp
public Task<TokenDataResult[]?> GetNFTsAsync(string symbol, IEnumerable<string> tokenIds, bool extended = false) => _rpc.SendRpcAsync<TokenDataResult[]>(Host, "getNFTs", symbol, string.Join(",", tokenIds), extended);
```

```csharp
public Task<TokenResult?> GetTokenAsync(string symbol) => _rpc.SendRpcAsync<TokenResult>(Host, "getToken", symbol);
```

```csharp
public Task<TokenResult?> GetTokenAsync(string symbol, bool extended, ulong carbonTokenId) => _rpc.SendRpcAsync<TokenResult>(Host, "getToken", symbol, extended, carbonTokenId);
```

```csharp
public Task<TokenResult[]?> GetTokensAsync() => _rpc.SendRpcAsync<TokenResult[]>(Host, "getTokens");
```

```csharp
public Task<TokenResult[]?> GetTokensAsync(bool extended, string? ownerAddress = null) => _rpc.SendRpcAsync<TokenResult[]>(Host, "getTokens", extended, ownerAddress);
```

```csharp
public Task<TokenResult[]?> GetTokensAsync(bool extended, string? ownerAddress, RpcAddressType addressType) => _rpc.SendRpcAsync<TokenResult[]>(Host, "getTokens", extended, ownerAddress, addressType);
```

```csharp
public Task<TokenSeriesResult?> GetTokenSeriesByIdAsync( string symbol = "", ulong carbonTokenId = 0, string seriesId = "", uint carbonSeriesId = 0) => _rpc.SendRpcAsync<TokenSeriesResult>( Host, "getTokenSeriesById", symbol, carbonTokenId, seriesId, carbonSeriesId);
```

```csharp
public Task<TransactionResult?> GetTransactionAsync(string txHash) => _rpc.SendRpcAsync<TransactionResult>(Host, "getTransaction", txHash);
```

```csharp
public Task<TransactionResult?> GetTransactionByBlockHashAndIndexAsync( string chainAddressOrName, string blockHash, int index) => _rpc.SendRpcAsync<TransactionResult>( Host, "getTransactionByBlockHashAndIndex", chainAddressOrName, blockHash, index);
```

```csharp
public Task<string?> LookUpNameAsync(string name) => _rpc.SendRpcAsync<string>(Host, "lookUpName", name);
```

```csharp
public Task<string?> ReadArchiveAsync(string hash, int blockIndex) => _rpc.SendRpcAsync<string>(Host, "readArchive", hash, blockIndex);
```

```csharp
public Task<string?> SendCarbonTransactionAsync(string txData) => _rpc.SendRpcAsync<string>(Host, "sendCarbonTransaction", txData);
```

```csharp
public Task<string?> SendRawTransactionAsync(string txData) => _rpc.SendRpcAsync<string>(Host, "sendRawTransaction", txData);
```

```csharp
public async Task<(AccountTransactionsResult? result, uint page, uint totalPages)> GetAddressTransactionsAsync(string address, uint page, uint pageSize)
```

```csharp
public async Task<(AuctionResult[]? result, uint page, uint total, uint totalPages)> GetAuctionsAsync(string chainAddressOrName, string symbol, uint page, uint pageSize)
```

```csharp
public async Task<bool> WriteArchiveAsync(string hash, int blockIndex, byte[] blockContent)
```

```csharp
public async Task<int> GetAddressTransactionCountAsync(string address, string chain)
```

```csharp
public async Task<int> GetAuctionsCountAsync(string chainAddressOrName, string symbol)
```

```csharp
public async Task<int> GetBlockTransactionCountByHashAsync(string chainAddressOrName, string blockHash)
```

```csharp
public async Task<long> GetBlockHeightAsync(string chain)
```

```csharp
public async Task<string?> SignAndSendCarbonTransactionAsync( IKeyPair keys, TxMsg txMsg)
```

```csharp
public async Task<string?> SignAndSendTransactionAsync( IKeyPair keys, string nexus, byte[] script, string chain, byte[] payload, Func<byte[], byte[], byte[], byte[]>? customSignFunction = null)
```

```csharp
public async Task<string?> SignAndSendTransactionAsync( IKeyPair keys, string nexus, byte[] script, string chain, string payload, Func<byte[], byte[], byte[], byte[]>? customSignFunction = null)
```

```csharp
public static bool IsValidAddress(string address)
```

```csharp
public static bool IsValidPrivateKey(string key)
```

```csharp
public string Host { get; }
```

```csharp
public void Dispose()
```

## PhantasmaPhoenix.RPC.RpcClient

Source: `PhantasmaPhoenix.RPC/src/RpcClient.cs`

### Declarations

```csharp
public sealed class RpcClient : IDisposable
```

### Methods

```csharp
public RpcClient(HttpClient? httpClient = null, ILogger? logger = null, int maxRetries = 0, int retryDelayMs = 1000)
```

```csharp
public async Task<T?> RestGetAsync<T>(string url)
```

```csharp
public async Task<T?> RestPostAsync<T>(string url, object body)
```

```csharp
public async Task<T?> SendRpcAsync<T>(string url, string method, params object[] parameters)
```

```csharp
public void Dispose()
```

## PhantasmaPhoenix.RPC.Types.CursorPaginatedResult

Source: `PhantasmaPhoenix.RPC/src/Types/CursorPaginatedResult.cs`

### Declarations

```csharp
public class CursorPaginatedResult<T>
```

### Methods

```csharp
public CursorPaginatedResult(T? result, string? cursor)
```

```csharp
public T? Result { get; set; }
```

```csharp
public string? Cursor { get; set; }
```

## PhantasmaPhoenix.RPC.Types.PaginatedResult

Source: `PhantasmaPhoenix.RPC/src/Types/PaginatedResult.cs`

### Declarations

```csharp
public class PaginatedResult<T>
```

### Methods

```csharp
public T? Result { get; set; }
```

```csharp
public uint Page { get; set; }
```

```csharp
public uint PageSize { get; set; }
```

```csharp
public uint Total { get; set; }
```

```csharp
public uint TotalPages { get; set; }
```

## PhantasmaPhoenix.RPC.Types.RpcAddressType

Source: `PhantasmaPhoenix.RPC/src/Types/RpcAddressType.cs`

### Declarations

```csharp
public enum RpcAddressType
```

### Variants

- `Carbon`
- `Phantasma`

## PhantasmaPhoenix.RPC.Types.RpcError

Source: `PhantasmaPhoenix.RPC/src/Types/RpcError.cs`

### Declarations

```csharp
public class RpcError
```

### Methods

```csharp
public RpcError()
```

```csharp
public RpcError(RpcErrorDescription rpcErrorDescription)
```

```csharp
public RpcError(RpcErrorDescription rpcErrorDescription, string additionalErrorInfo)
```

```csharp
public RpcError(int code, string message)
```

```csharp
public int Code { get; set; }
```

```csharp
public string Message { get; set; }
```

## PhantasmaPhoenix.RPC.Types.RpcErrorDescription

Source: `PhantasmaPhoenix.RPC/src/Types/RpcError.cs`

### Declarations

```csharp
public class RpcErrorDescription
```

### Methods

```csharp
public HttpStatusCode HttpCode { get; set; }
```

```csharp
public RpcErrorDescription(int code, string message, HttpStatusCode httpCode)
```

```csharp
public int Code { get; set; }
```

```csharp
public string Message { get; set; }
```

## PhantasmaPhoenix.RPC.Types.RpcErrors

Source: `PhantasmaPhoenix.RPC/src/Types/RpcError.cs`

### Declarations

```csharp
public static class RpcErrors
```

### Methods

```csharp
public const int RPC_ERROR_IMPLEMENTATION = -32000;
```

```csharp
public const int RPC_ERROR_INTERNAL = -32603;
```

```csharp
public const int RPC_ERROR_INVALID = -32600;
```

```csharp
public const int RPC_ERROR_METHOD = -32601;
```

```csharp
public const int RPC_ERROR_PARAMS = -32602;
```

```csharp
public const int RPC_ERROR_PARSE = -32700;
```

```csharp
public static Dictionary<int, RpcErrorDescription> errors = new()
```

```csharp
public static RpcErrorDescription GetDescription(int code)
```

## PhantasmaPhoenix.RPC.Types.RpcId

Source: `PhantasmaPhoenix.RPC/src/Types/RpcId.cs`

### Declarations

```csharp
public sealed class RpcId : IEquatable<RpcId>
```

### Methods

```csharp
public JToken Value => _value.DeepClone();
```

```csharp
public RpcId(int value) : this((long)value)
```

```csharp
public RpcId(long value)
```

```csharp
public RpcId(string value)
```

```csharp
public bool Equals(RpcId? other)
```

```csharp
public override bool Equals(object? obj)
```

```csharp
public override int GetHashCode()
```

```csharp
public override string ToString()
```

```csharp
public static RpcId FromJsonToken(JToken value)
```

```csharp
public static implicit operator RpcId(int value)
```

```csharp
public static implicit operator RpcId(long value)
```

```csharp
public static implicit operator RpcId(string value)
```

## PhantasmaPhoenix.RPC.Types.RpcRequest

Source: `PhantasmaPhoenix.RPC/src/Types/RpcRequest.cs`

### Declarations

```csharp
public struct RpcRequest
```

### Methods

```csharp
public RpcId? id { get; set; }
```

```csharp
public object[] @params { get; set; }
```

```csharp
public override string ToString()
```

```csharp
public string jsonrpc { get; set; }
```

```csharp
public string method { get; set; }
```

## PhantasmaPhoenix.RPC.Types.RpcResponse

Source: `PhantasmaPhoenix.RPC/src/Types/RpcResponse.cs`

### Declarations

```csharp
public class RpcResponse
```

### Methods

```csharp
public RpcError? Error { get; set; }
```

```csharp
public RpcId? id { get; set; }
```

```csharp
public RpcResponse()
```

```csharp
public RpcResponse(RpcId? id, object? result, RpcError? error)
```

```csharp
public object? Result { get; set; }
```

```csharp
public string jsonrpc { get; set; } = "2.0";
```

## PhantasmaPhoenix.VM.ExecutionContext

Source: `PhantasmaPhoenix.VM/src/Data/ExecutionContext.cs`

### Declarations

```csharp
public abstract class ExecutionContext
```

### Methods

```csharp
public Address Address
```

```csharp
public abstract ExecutionState Execute(ExecutionFrame frame, Stack<VMObject> stack);
```

```csharp
public abstract string Name { get; }
```

```csharp
public override string ToString()
```

## PhantasmaPhoenix.VM.ExecutionFrame

Source: `PhantasmaPhoenix.VM/src/Data/ExecutionFrame.cs`

### Declarations

```csharp
public class ExecutionFrame
```

### Methods

```csharp
public ExecutionContext Context { get; }
```

```csharp
public ExecutionFrame(IVirtualMachine vm, uint offset, ExecutionContext context, int registerCount)
```

```csharp
public IVirtualMachine VM { get; }
```

```csharp
public VMObject GetRegister(int index)
```

```csharp
public VMObject[] Registers { get; }
```

```csharp
public uint Offset { get; }
```

## PhantasmaPhoenix.VM.IVirtualMachine

Source: `PhantasmaPhoenix.VM/src/Data/IVirtualMachine.cs`

### Declarations

```csharp
public interface IVirtualMachine
```

### Methods

```csharp
public Address EntryAddress { get; set; }
```

```csharp
public ExecutionContext CurrentContext { get; set; }
```

```csharp
public ExecutionContext FindContext(string contextName);
```

```csharp
public ExecutionContext PreviousContext { get; set; }
```

```csharp
public ExecutionFrame CurrentFrame { get; set; }
```

```csharp
public ExecutionFrame PeekFrame();
```

```csharp
public ExecutionState Execute();
```

```csharp
public ExecutionState ExecuteInterop(string method);
```

```csharp
public ExecutionState SwitchContext(ExecutionContext context, uint instructionPointer);
```

```csharp
public ExecutionState ValidateOpcode(Opcode opcode);
```

```csharp
public Stack<ExecutionFrame> Frames { get; }
```

```csharp
public Stack<VMObject> Stack { get; }
```

```csharp
public abstract ExecutionContext LoadContext(string contextName);
```

```csharp
public byte[] EntryScript { get; }
```

```csharp
public string GetDumpFileName();
```

```csharp
public uint PopFrame();
```

```csharp
public void DumpData(List<string> lines);
```

```csharp
public void Expect(bool condition, string description);
```

```csharp
public void PushFrame(ExecutionContext context, uint instructionPointer, int registerCount);
```

```csharp
public void RegisterContext(string contextName, ExecutionContext context);
```

```csharp
public void SetCurrentContext(ExecutionContext context);
```

## PhantasmaPhoenix.VM.VMType

Source: `PhantasmaPhoenix.VM/src/Data/VMObject.cs`

### Declarations

```csharp
public enum VMType
```

### Variants

- `Bool`
- `Bytes`
- `Enum`
- `None`
- `Number`
- `Object`
- `String`
- `Struct`
- `Timestamp`

## PhantasmaPhoenix.VM.VMObject

Source: `PhantasmaPhoenix.VM/src/Data/VMObject.cs`

### Declarations

```csharp
public sealed class VMObject : ISerializable
```

### Methods

```csharp
public Address AsAddress()
```

```csharp
public BigInteger AsNumber()
```

```csharp
public Dictionary<VMObject, VMObject> GetChildren() => this.Type == VMType.Struct ? (Dictionary<VMObject, VMObject>)Data : null;
```

```csharp
public T AsEnum<T>() where T : struct, IConvertible
```

```csharp
public T AsInterop<T>()
```

```csharp
public T AsStruct<T>()
```

```csharp
public T ToStruct<T>()
```

```csharp
public T[] ToArray<T>()
```

```csharp
public Timestamp AsTimestamp()
```

```csharp
public VMObject GetKey(VMObject key)
```

```csharp
public VMObject SetDefaultValue(VMType type)
```

```csharp
public VMObject SetValue(Address address)
```

```csharp
public VMObject SetValue(BigInteger val)
```

```csharp
public VMObject SetValue(DateTime val)
```

```csharp
public VMObject SetValue(Dictionary<VMObject, VMObject> children)
```

```csharp
public VMObject SetValue(Enum val)
```

```csharp
public VMObject SetValue(Hash hash)
```

```csharp
public VMObject SetValue(Timestamp val)
```

```csharp
public VMObject SetValue(bool val)
```

```csharp
public VMObject SetValue(byte[] val)
```

```csharp
public VMObject SetValue(byte[] val, VMType type)
```

```csharp
public VMObject SetValue(object val)
```

```csharp
public VMObject SetValue(string val)
```

```csharp
public VMObject()
```

```csharp
public VMObject[] AsArray(VMType type)
```

```csharp
public VMType GetArrayType()
```

```csharp
public VMType Type { get; private set; }
```

```csharp
public bool AsBool()
```

```csharp
public bool IsEmpty => Data == null;
```

```csharp
public byte[] AsByteArray()
```

```csharp
public int Size
```

```csharp
public object AsType(VMType type)
```

```csharp
public object Data { get; private set; }
```

```csharp
public object ToArray(Type arrayElementType)
```

```csharp
public object ToObject()
```

```csharp
public object ToObject(Type type)
```

```csharp
public object ToStruct(Type structType)
```

```csharp
public override bool Equals(object obj)
```

```csharp
public override int GetHashCode()
```

```csharp
public override string ToString()
```

```csharp
public static VMObject CastTo(VMObject srcObj, VMType type)
```

```csharp
public static VMObject FromArray(Array array)
```

```csharp
public static VMObject FromBytes(byte[] bytes)
```

```csharp
public static VMObject FromObject(object obj)
```

```csharp
public static VMObject FromStruct(object obj)
```

```csharp
public static VMType GetVMType(Type type)
```

```csharp
public static bool IsVMType(Type type)
```

```csharp
public string AsString()
```

```csharp
public void Copy(VMObject other)
```

```csharp
public void SerializeData(BinaryWriter writer)
```

```csharp
public void SetKey(VMObject key, VMObject obj)
```

```csharp
public void UnserializeData(BinaryReader reader)
```

```csharp
public void UnserializeData(byte[] bytes)
```

## PhantasmaPhoenix.VM.GasMachine

Source: `PhantasmaPhoenix.VM/src/Execution/GasMachine.cs`

### Declarations

```csharp
public class GasMachine : VirtualMachine
```

### Methods

```csharp
public BigInteger UsedGas { get; protected set; }
```

```csharp
public GasMachine(byte[] script, uint offset, string contextName = null) : base(script, offset, contextName)
```

```csharp
public override ExecutionContext LoadContext(string contextName)
```

```csharp
public override ExecutionState ExecuteInterop(string method)
```

```csharp
public override ExecutionState ValidateOpcode(Opcode opcode)
```

```csharp
public override void DumpData(List<string> lines)
```

```csharp
public static BigInteger GetGasCostForOpcode(Opcode opcode)
```

```csharp
public virtual ExecutionState ConsumeGas(BigInteger gasCost)
```

## PhantasmaPhoenix.VM.VirtualMachine

Source: `PhantasmaPhoenix.VM/src/Execution/VirtualMachine.cs`

### Declarations

```csharp
public abstract class VirtualMachine : IVirtualMachine
```

### Methods

```csharp
public Address EntryAddress
```

```csharp
public ExecutionContext CurrentContext { get; set; }
```

```csharp
public ExecutionContext EntryContext => entryContext;
```

```csharp
public ExecutionContext PreviousContext { get; set; }
```

```csharp
public ExecutionFrame CurrentFrame { get; set; }
```

```csharp
public ExecutionFrame PeekFrame()
```

```csharp
public Stack<Address> ActiveAddresses => _activeAddresses;
```

```csharp
public Stack<ExecutionFrame> Frames { get { return frames; } }
```

```csharp
public Stack<VMObject> Stack { get; } = new Stack<VMObject>();
```

```csharp
public VirtualMachine(byte[] script, uint offset, string contextName)
```

```csharp
public abstract ExecutionContext LoadContext(string contextName);
```

```csharp
public abstract ExecutionState ExecuteInterop(string method);
```

```csharp
public abstract void DumpData(List<string> lines);
```

```csharp
public byte[] EntryScript { get; }
```

```csharp
public const int DefaultRegisterCount = 32;
```

```csharp
public const int MaxRegisterCount = 32;
```

```csharp
public readonly static string EntryContextName = "entry";
```

```csharp
public readonly static string ExchangeContextName = "exchange";
```

```csharp
public readonly static string GasContextName = "gas";
```

```csharp
public readonly static string StakeContextName = "stake";
```

```csharp
public virtual ExecutionContext FindContext(string contextName)
```

```csharp
public virtual ExecutionState Execute()
```

```csharp
public virtual ExecutionState SwitchContext(ExecutionContext context, uint instructionPointer)
```

```csharp
public virtual ExecutionState ValidateOpcode(Opcode opcode)
```

```csharp
public virtual string GetDumpFileName()
```

```csharp
public virtual uint PopFrame()
```

```csharp
public void Expect(bool condition, string description)
```

```csharp
public void PushFrame(ExecutionContext context, uint instructionPointer, int registerCount)
```

```csharp
public void RegisterContext(string contextName, ExecutionContext context)
```

```csharp
public void SetCurrentContext(ExecutionContext context)
```

## PhantasmaPhoenix.VM.VMException

Source: `PhantasmaPhoenix.VM/src/Execution/VirtualMachine.cs`

### Declarations

```csharp
public class VMException : Exception
```

### Methods

```csharp
public IVirtualMachine vm;
```

```csharp
public VMException(IVirtualMachine vm, string msg) : base(msg)
```

```csharp
public static string Header(string s)
```

## PhantasmaPhoenix.VM.Instruction

Source: `PhantasmaPhoenix.VM/src/Script/Instruction.cs`

### Declarations

```csharp
public struct Instruction
```

### Methods

```csharp
public Opcode Opcode;
```

```csharp
public object[] Args;
```

```csharp
public override string ToString()
```

```csharp
public uint Offset;
```

## PhantasmaPhoenix.VM.Opcode

Source: `PhantasmaPhoenix.VM/src/Script/Opcodes.cs`

### Declarations

```csharp
public enum Opcode
```

### Variants

- `ABS`
- `ADD`
- `AND`
- `CALL`
- `CAST`
- `CAT`
- `CLEAR, // clears a register`
- `COPY,   // copy by value`
- `COUNT`
- `CTX`
- `DEBUG`
- `DEC`
- `DIV`
- `EQUAL`
- `EXTCALL`
- `GET, // lookups a key and copies a reference into register`
- `GT`
- `GTE`
- `INC`
- `JMP`
- `JMPIF`
- `JMPNOT`
- `LEFT`
- `LOAD`
- `LT`
- `LTE`
- `MAX`
- `MIN`
- `MOD`
- `MOVE,    // copy reference`
- `MUL`
- `NEGATE`
- `NOP`
- `NOT`
- `OR`
- `PACK, // unused for now`
- `POP`
- `POW`
- `PUSH`
- `PUT`
- `RANGE`
- `RET`
- `RIGHT`
- `SHL`
- `SHR`
- `SIGN`
- `SIZE`
- `SUB`
- `SUBSTR`
- `SWAP`
- `SWITCH`
- `THROW`
- `UNPACK, // unpacks serialized struct based on ref struct`
- `XOR`

## PhantasmaPhoenix.VM.ScriptBuilder

Source: `PhantasmaPhoenix.VM/src/Script/ScriptBuilder.cs`

### Declarations

```csharp
public class ScriptBuilder
```

### Methods

```csharp
public ScriptBuilder Emit(Opcode opcode, byte[] bytes = null)
```

```csharp
public ScriptBuilder EmitCall(string label, byte regCount)
```

```csharp
public ScriptBuilder EmitConditionalJump(Opcode opcode, byte src_reg, string label)
```

```csharp
public ScriptBuilder EmitCopy(byte src_reg, byte dst_reg)
```

```csharp
public ScriptBuilder EmitExtCall(string method, byte reg = 0)
```

```csharp
public ScriptBuilder EmitJump(Opcode opcode, string label, byte reg = 0)
```

```csharp
public ScriptBuilder EmitLabel(string label)
```

```csharp
public ScriptBuilder EmitLoad(byte reg, BigInteger val)
```

```csharp
public ScriptBuilder EmitLoad(byte reg, Enum val)
```

```csharp
public ScriptBuilder EmitLoad(byte reg, ISerializable val)
```

```csharp
public ScriptBuilder EmitLoad(byte reg, Timestamp val)
```

```csharp
public ScriptBuilder EmitLoad(byte reg, bool val)
```

```csharp
public ScriptBuilder EmitLoad(byte reg, byte[] bytes, VMType type = VMType.Bytes)
```

```csharp
public ScriptBuilder EmitLoad(byte reg, string val)
```

```csharp
public ScriptBuilder EmitMove(byte src_reg, byte dst_reg)
```

```csharp
public ScriptBuilder EmitPop(byte reg)
```

```csharp
public ScriptBuilder EmitPush(byte reg)
```

```csharp
public ScriptBuilder EmitRaw(byte[] bytes)
```

```csharp
public ScriptBuilder EmitThrow(byte reg)
```

```csharp
public ScriptBuilder EmitVarBytes(long value)
```

```csharp
public ScriptBuilder()
```

```csharp
public byte[] ToScript()
```

```csharp
public byte[] ToScript(out Dictionary<string, int> labels)
```

```csharp
public int CurrentSize => (int)writer.BaseStream.Position;
```

## PhantasmaPhoenix.VM.ScriptBuilderExtensions

Source: `PhantasmaPhoenix.VM/src/Script/ScriptBuilderExtensions.cs`

### Declarations

```csharp
public static class ScriptBuilderExtensions
```

### Methods

```csharp
public static ScriptBuilder AllowGas(this ScriptBuilder sb, Address from, Address to, BigInteger gasPrice, BigInteger gasLimit)
```

```csharp
public static ScriptBuilder CallContract(this ScriptBuilder sb, NativeContractKind contractKind, string method, params object[] args)
```

```csharp
public static ScriptBuilder CallNFT(this ScriptBuilder sb, string symbol, BigInteger seriesID, string method, params object[] args)
```

```csharp
public static ScriptBuilder CrossTransferNFT(this ScriptBuilder sb, Address destinationChain, string tokenSymbol, Address from, Address to, BigInteger tokenId)
```

```csharp
public static ScriptBuilder CrossTransferNFT(this ScriptBuilder sb, Address destinationChain, string tokenSymbol, Address from, string to, BigInteger tokenId)
```

```csharp
public static ScriptBuilder CrossTransferToken(this ScriptBuilder sb, Address destinationChain, string tokenSymbol, Address from, Address to, BigInteger amount)
```

```csharp
public static ScriptBuilder CrossTransferToken(this ScriptBuilder sb, Address destinationChain, string tokenSymbol, Address from, string to, BigInteger amount)
```

```csharp
public static ScriptBuilder MintTokens(this ScriptBuilder sb, string tokenSymbol, Address from, Address target, BigInteger amount)
```

```csharp
public static ScriptBuilder SpendGas(this ScriptBuilder sb, Address address)
```

```csharp
public static ScriptBuilder TransferBalance(this ScriptBuilder sb, string tokenSymbol, Address from, Address to)
```

```csharp
public static ScriptBuilder TransferNFT(this ScriptBuilder sb, string tokenSymbol, Address from, Address to, BigInteger tokenId)//todo check if this is valid
```

```csharp
public static ScriptBuilder TransferNFT(this ScriptBuilder sb, string tokenSymbol, Address from, string to, BigInteger tokenId)//todo check if this is valid
```

```csharp
public static ScriptBuilder TransferTokens(this ScriptBuilder sb, string tokenSymbol, Address from, Address to, BigInteger amount)
```

```csharp
public static ScriptBuilder TransferTokens(this ScriptBuilder sb, string tokenSymbol, Address from, string to, BigInteger amount)
```

## PhantasmaPhoenix.VM.ScriptContext

Source: `PhantasmaPhoenix.VM/src/Script/ScriptContext.cs`

### Declarations

```csharp
public class ScriptContext : ExecutionContext
```

### Methods

```csharp
public ScriptContext(string name, byte[] script, uint offset)
```

```csharp
public byte[] Script { get; private set; }
```

```csharp
public override ExecutionState Execute(ExecutionFrame frame, Stack<VMObject> stack)
```

```csharp
public override string Name => _name;
```

```csharp
public static readonly byte[] EmptyScript = new byte[] { (byte)Opcode.RET };
```

```csharp
public string Error { get; private set; }
```

```csharp
public uint InstructionPointer { get; private set; }
```

```csharp
public void Step(ref ExecutionFrame frame, Stack<VMObject> stack)
```

## PhantasmaPhoenix.VM.ScriptUtils

Source: `PhantasmaPhoenix.VM/src/Script/ScriptUtils.cs`

### Declarations

```csharp
public static class ScriptUtils
```

### Methods

```csharp
public static ScriptBuilder BeginScript()
```

```csharp
public static ScriptBuilder CallContract(this ScriptBuilder sb, string contractName, string method, params object[] args)
```

```csharp
public static ScriptBuilder CallInterop(this ScriptBuilder sb, string method, params object[] args)
```

```csharp
public static byte[] EndScript(this ScriptBuilder sb)
```

## PhantasmaPhoenix.VM.DisasmMethodCall

Source: `PhantasmaPhoenix.VM/src/Tools/DisasmUtils.cs`

### Declarations

```csharp
public struct DisasmMethodCall
```

### Methods

```csharp
public VMObject[] Arguments;
```

```csharp
public override string ToString()
```

```csharp
public string ContractName;
```

```csharp
public string MethodName;
```

```csharp
public string ToString(bool useNewlines)
```

## PhantasmaPhoenix.VM.DisasmUtils

Source: `PhantasmaPhoenix.VM/src/Tools/DisasmUtils.cs`

### Declarations

```csharp
public static class DisasmUtils
```

### Methods

```csharp
public static Dictionary<string, int> GetDefaultDisasmTable()
```

```csharp
public static IEnumerable<DisasmMethodCall> ExtractMethodCalls(Disassembler disassembler, Dictionary<string, int> methodArgumentCountTable)
```

```csharp
public static IEnumerable<DisasmMethodCall> ExtractMethodCalls(byte[] script, Dictionary<string, int> methodArgumentCountTable)
```

```csharp
public static IEnumerable<string> ExtractContractNames(Disassembler disassembler)
```

```csharp
public static IEnumerable<string> ExtractContractNames(byte[] script)
```

## PhantasmaPhoenix.VM.Disassembler

Source: `PhantasmaPhoenix.VM/src/Tools/Disassembler.cs`

### Declarations

```csharp
public class Disassembler
```

### Methods

```csharp
public Disassembler(byte[] script)
```

```csharp
public IEnumerable<Instruction> Instructions => _instructions.AsReadOnly();
```

```csharp
public override string ToString()
```

## PhantasmaPhoenix.VM.Validation

Source: `PhantasmaPhoenix.VM/src/Tools/ValidationUtils.cs`

### Declarations

```csharp
public static class Validation
```

### Methods

```csharp
public static bool IsValidMethod(string methodName, VMType returnType)
```
