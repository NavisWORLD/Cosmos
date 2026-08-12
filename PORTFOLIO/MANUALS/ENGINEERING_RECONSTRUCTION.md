# Engineering Reconstruction Manual

A prototype is treated as ancestry, audited aggressively, and rebuilt into a defensible system rather than merely redesigned visually.

## Workflow
1. Preserve/hash original.
2. Extract claims: voltage/current/power, PWM, ratings, timing, thermal limits, rates, dimensions, platform/API behavior.
3. Derive requirements independently from physics/datasheets/standards/platform limits.
4. Build contradiction table: claim → required evidence → finding → action.
5. Rebuild architecture separating power, control, signal, safety, firmware/software, UI/telemetry, external dependencies.
6. Analyze failures: short/open, brownout, heat, invalid/stale data, disconnect, exception, race/file lock, malformed input.
7. Instrument values a technician can inspect.
8. Validate simulation → bench → subsystem → full-load → long-run/thermal.

Novel presentation is welcome; fabricated component behavior is not.
