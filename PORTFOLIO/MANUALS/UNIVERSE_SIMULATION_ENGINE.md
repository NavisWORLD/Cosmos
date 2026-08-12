# Universe Simulation Engine Manual

## Goal
Turn CST/COSMOS ideas into an explorable deterministic world system: generate/import astronomical systems, advance orbital state, descend through scales, render environments, and expose world state to Python/C++ and game/render loops.

The complete standalone package is a [publication gap](../PUBLICATION_GAPS.md) until canonical files are verified/committed.

## Principles
- deterministic universe seed
- explicit distinction between imported, derived, procedural, and visual-approximation data
- multi-scale representations: system → orbital → body → surface → gameplay
- stable units/reference frames

## C++ core
Vector/quaternion math, deterministic PRNG streams, ECS/world state, orbital/physics stepping, spatial partitioning, terrain chunks, collisions, high-frequency fixed tick, serialization.

## Python layer
Catalog/data ingestion, NASA/APOD metadata adapters, USGS/geospatial preprocessing where relevant, procedural authoring, experiments, batch generation, validation, asset prep, COSMOS control integration.

## Fixed simulation loop
```text
accumulator += frame_dt
while accumulator >= fixed_dt:
  sample queued controls
  advance deterministic physics/world systems
  emit state snapshot
  accumulator -= fixed_dt
```
Rendering interpolates snapshots separately.

## Scale precision
Use hierarchical frames, origin rebasing/camera-relative rendering, double precision for astronomical state, local floats for GPU chunks, and explicit units.

## Procedural streams
`system_seed → body_seed → terrain_seed → biome_seed → object/ecology_seed`
Separate PRNG streams so a decoration change does not alter an orbit.

## APOD
Treat APOD as media/metadata inspiration or adapter, not as a full physical universe catalog. Cache data, preserve source metadata, and keep network failure outside deterministic simulation.

## Rendering
PBR, HDR/tonemapping, atmosphere approximation, procedural sky/star rendering, terrain LOD, temporal interpolation, instancing/compute where appropriate, and quality tiers.

## CST integration
12D/42D/54D may act as experimental latent control/state for agents, music, UI, procedural modulation, or telemetry. It is not a replacement for physical coordinates.

## World export
Seed, generator version/hash, source IDs/timestamps, units/frames, initial orbital state, procedural version, timestep, control-state configuration.
