**Threshold Path – Hex Entry Sequence (v2)**

This document defines the step-by-step protocol for generating a new hex upon entry within the Threshold Path.

---

### 🧭 Hex Entry Sequence

1. Receive **entry direction** (from previous hex's exit)
2. **Pick one exit direction**, excluding the entry direction
3. **Check for forks**:

   * Roll d10
   * If result is 1, create a fork
4. If fork, **assign a new direction** (excluding used ones), then:

   * Roll d10 again
   * Repeat step 4 on result of 1 (max 7 exits total)
5. Create **Hex ID**
6. Apply **biome, terrain, and feature** (using continuity logic)
7. Repeat steps 1–6 for **each forward hex** at all exits (excluding entrance)
8. **Terrain** matches previous hex with 90% probability
9. **Feature** matches previous hex with 75% probability
10. Generate **narrative title and prose** (based on symbolic synthesis)
11. Display **exit list** beneath the narrative block, labeled by compass direction

---

This sequence ensures each hex retains logical continuity while enabling symbolic divergence and rare branching. All forward paths must be resolved in advance of entry.
