# Music Systems & Alien Conductor Manual

## Core idea
Human gesture and media become musical structure rather than simple buttons.

Inputs may include touch, device motion, microphone energy/pitch/spectrum, singing/instrument input, MIDI, camera light/motion summaries, uploaded media, and optional aggregated biosignals through an explicit device bridge.

## Mobile browser audio boot
On iOS/mobile, create/resume `AudioContext` inside an explicit user gesture, initialize the graph, verify context is `running`, then start sequencers/mic-driven synthesis. This is a common cause of “UI works but no sound.”

## Audio graph
`analyzers → feature/state → conductor/harmony/rhythm → generators → envelopes/filters → submix → effects/dynamics → master`

## Play-along
Estimate activity/onsets, pitch class/key center, pulse confidence, spectral density, phrase boundaries, dynamics. Generate support/counterpoint/drone/percussion/bass/pad/call-response rather than merely copying detected pitch.

## Sensor mapping
Use smoothing, hysteresis, dead zones, confidence gates, rate limits, and musical quantization. Avoid mapping raw noisy sensor channels directly to unstable audio parameters.

## CST state
12D state can be an experimental latent control surface for timbre, density, harmony probability, effect sends, or conductor policy. This is an artistic/computational mapping unless benchmarked separately.

## Biosignal bridge
A browser cannot assume direct Apple Watch/HealthKit access. Use an authorized native/device bridge exposing only required aggregate signals with explicit permissions/retention.

## Timing
Schedule audio against the audio clock; use visual frames for UI/visualization, not sample-accurate musical events.

## Tech
- [12D Cosmic Synapse Audio Engine demo](../../12D_Cosmic_Synapse_Audio_Engine-demo.html)
- [Publication gaps](../PUBLICATION_GAPS.md)
