---
cover: .gitbook/assets/gitbook-banner-pha-phoenix-godot-sdk.png
coverY: 0
---
# Using a Standard C# SDK in Godot (Godot .NET)

> This page shows how to add and use any regular C#/.NET SDK (distributed as a NuGet package or a DLL) inside a Godot 4 project that uses C#. It assumes you’re using the **.NET build** of the Godot editor.

## Prerequisites

* Install the **Godot .NET** editor build (not the standard build) ([Godot Engine Documentation][1])
* Install **.NET SDK 8.0 or newer** (Godot 4.4 targets .NET 8 by default, but .NET 9.0 is also supported and recommended) ([Godot Engine][2], [Godot Engine Documentation][3])
* An IDE that supports C# (VS Code, Rider, or Visual Studio)

## Create or enable a C# project

1. Open Godot (.NET) → create a project
2. Add your first C# script (Godot will generate a `*.csproj` for you)
3. Build once to let Godot restore packages and generate bindings ([Godot Engine Documentation][4])

## Add Phantasma Phoenix C# SDK

### Option A — via NuGet (recommended)

From your project folder (where the `.csproj` lives), add the package (PhantasmaPhoenix.Cryptography shown here as an example, check [this](/developers/sdks/csharp/setup.md) page for full list of available packages):

```bash
dotnet add package PhantasmaPhoenix.Cryptography
dotnet restore
```

Godot C# uses standard .NET projects, so NuGet packages work the same way as in any C# app ([Godot Engine Documentation][1])

### Option B — reference a local DLL

If you have a compiled `PhantasmaPhoenix.Cryptography.dll`, add a reference in your `.csproj`:

```xml
<ItemGroup>
  <Reference Include="PhantasmaPhoenix.Cryptography">
    <HintPath>addons/PhantasmaPhoenix.Cryptography.dll</HintPath>
  </Reference>
</ItemGroup>
```

Godot recognizes regular C# project references; external managed DLLs can be added in the `.csproj` file ([Godot Forums][5], [Reddit][6])

## Minimal example

Create `Scripts/ExampleSdkUsage.cs` and attach it to a Node:

```csharp
using Godot;
using PhantasmaPhoenix.Cryptography;

public partial class ExampleSdkUsage : Node
{
    public override void _Ready()
    {
       	var keys = PhantasmaKeys.Generate();
        GD.Print($"Address: {keys.Address.Text}");
    }
}
```

Build the project (from IDE or `dotnet build`) and run the scene.
C# scripts and exported members behave like in regular Godot C# projects ([Godot Engine Documentation][1])

## Exporting the game (with C#)

1. Install export templates in Godot
2. Configure an export preset (Windows, Linux, macOS, Android, iOS)
3. Export your build

See **Exporting projects** in the official docs for platform setup and templates ([Godot Engine Documentation][7])

> Note: Web (HTML5) export with C# is not supported in Godot 4.x at the time of writing ([Godot Forum][8])

## Tips & troubleshooting

* Make sure your project targets **`net9.0`** in the `.csproj` when using Godot 4.4 packages:

  ```xml
  <PropertyGroup>
    <TargetFramework>net9.0</TargetFramework>
  </PropertyGroup>
  ```

  Details: GodotSharp packages moved to .NET 8 in 4.4 ([Godot Engine][2])
* If NuGet restore fails, verify your **NuGet configuration** or regenerate `NuGet.Config` (common fix for `Godot.NET.Sdk` not found) ([Reddit][9])
* Godot uses the `Godot.NET.Sdk` MSBuild SDK in your `.csproj` (managed by Godot) ([NuGet][10])
* General C#/.NET how‑to for Godot (language features, exports, etc.) is covered in the official C# docs ([Godot Engine Documentation][1])

## Useful links

* Godot C#/.NET docs (overview & basics) ([Godot Engine Documentation][1])
* C# basics (4.4) and exports (attributes) ([Godot Engine Documentation][11])
* Exporting projects (templates & presets) ([Godot Engine Documentation][7])
* GodotSharp packages & .NET 8 note (Godot 4.4) ([Godot Engine][2])
* Platform state of C# in Godot 4.x (what “standard .NET” means) ([Godot Engine][12])

---

[1]: https://docs.godotengine.org/en/4.4/tutorials/scripting/c_sharp/index.html "C#/.NET — Godot Engine (4.4) documentation in English"
[2]: https://godotengine.org/article/godotsharp-packages-net8 "Godot C# packages move to .NET 8"
[3]: https://docs.godotengine.org/en/4.3/development/compiling/compiling_with_mono.html "Compiling with .NET — Godot Engine (4.3) documentation in ..."
[4]: https://docs.godotengine.org/en/4.3/tutorials/scripting/c_sharp/c_sharp_basics.html "C# basics — Godot Engine (4.3) documentation in English"
[5]: https://godotforums.org/d/38934-how-to-reference-a-library-managed-dll-in-a-c-addon "How to reference a library ( managed DLL) in a C# addon"
[6]: https://www.reddit.com/r/godot/comments/19cck6e/how_to_use_c_godot_nodes_from_external_library "How to use C# Godot Nodes from external library (nuget ..."
[7]: https://docs.godotengine.org/en/latest/tutorials/export/exporting_projects.html "Exporting projects - Godot Docs"
[8]: https://forum.godotengine.org/t/c-godot-4-and-html5-possible-when/97253 "C# Godot 4 and HTML5 - possible when? - Help"
[9]: https://www.reddit.com/r/godot/comments/1f1kucp/why_is_so_hard_to_make_godot_43_c_working_i "Why is so hard to make godot 4.3 c# working? i instal ..."
[10]: https://www.nuget.org/packages/Godot.NET.Sdk "Godot.NET.Sdk 4.4.1"
[11]: https://docs.godotengine.org/en/4.4/tutorials/scripting/c_sharp/c_sharp_basics.html "C# basics — Godot Engine (4.4) documentation in English"
[12]: https://godotengine.org/article/platform-state-in-csharp-for-godot-4-2 "Current state of C# platform support in Godot 4.2"
