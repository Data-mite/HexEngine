**Threshold Path: Hex Generation Protocol (v3)**

This document defines the complete and correct sequence for generating and displaying hexes within the Threshold Path system. It expands on prior logic and formalizes expectations for traversal, continuity, and narrative formatting.

---

### 📍 Hex Generation Rules

* Every hex is a narrative unit in a procedurally generated liminal travel space.
* Each hex has a unique ID, one entry direction, and **1–7 total exits**, excluding entry.
* Directions use an 8-point compass: N, NE, E, SE, S, SW, W, NW.

### 🔁 Fork Logic

1. **One forward exit** is always generated (excluding the entry direction).
2. Roll **d10**:

   * On a result of `1`, a fork occurs.
   * Repeat this step for each new fork. Stop if the result is not `1`.
   * Maximum exits = 7 total (including the one used for entry).

### 🌐 Terrain Continuity Rules

* **Biome** is usually fixed for a path segment unless rerolled.
* **Terrain** matches the previous hex with **90% probability**.
* If terrain changes:

  * Roll d20 on the appropriate `HG_Terrain_<Biome>` table.
* **Feature** matches previous with **75% probability**.
* If feature changes:

  * Roll d20 on `HG_Feature_<Biome>_<Terrain>`.

### 🧭 Entry Sequence (Hex Creation)

1. **Receive entry direction** from the previous hex’s exit.
2. **Generate exits** using fork logic (excluding entry direction).
3. **Generate terrain and feature**, applying continuity probability rules.
4. **Assign unique hex ID**.
5. **Create forward hexes** for each new exit (excluding entry).
6. **Store directional continuity**.
7. **Apply terrain feature hints** to forward exits (short, abstracted).
8. **Format and display hex using canonical narrative structure.**

---

### 🧾 Canonical Narrative Block Format

Each hex is rendered as follows:

#### \[Evocative Hex Title]

\[3–5 lines of immersive narrative prose. Should reflect biome, terrain, feature, and mood.]

* **Exits:**

  * `[Direction] - (Back) [Title of Previous Hex]` *(if applicable)*
  * `[Direction] - [Terrain] [Short, abstracted feature hint]`

Example:

### The Slope With No Witness

The path shears sideways along a brittle slope, too narrow for certainty.
In the distance, shapes move—indifferent, four-legged, adapted to heights you haven’t earned.
No trail marks your passage. Just loose stone, and the air, watching.

* **Exits:**

  * `SE - (Back) The Memory That Trails`
  * `W - Alpine [Something moves, but not for you]`

---

This protocol must be followed for each new hex generated in the Threshold Path system.
