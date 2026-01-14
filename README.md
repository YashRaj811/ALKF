# 🏗️ Layout Generator Assignment

## 📌 Overview
This project implements an automated **layout generation and visualization tool** for a rectangular site.  
The program explores multiple building configurations while enforcing geometric, spacing, and proximity rules.

It generates **clear visual outputs** that make it easy to compare layouts and verify rule compliance.

---

## 📐 Site & Building Configuration

### Site
- Size: **200 m × 140 m**
- Coordinate System: `(0,0)` bottom-left → `(200,140)` top-right

### Building Types
| Type | Footprint |
|-----|-----------|
| Tower A | 30 m × 20 m |
| Tower B | 20 m × 20 m |

### Central Plaza
- Size: **40 m × 40 m**
- Location: Center of the site
- Constraint: No buildings may overlap this area

---

## 📏 Placement Rules
The following rules are enforced during layout generation:

1. All buildings must be fully inside the site.
2. Minimum distance between any two buildings: **15 m (edge-to-edge)**.
3. Minimum distance from any building to the site boundary: **10 m**.
4. **Neighbour-mix rule**:  
   Every Tower A must have at least **one Tower B within 60 m**.
5. No building footprint may overlap the central plaza.

---

## 🧠 Methodology
- Uses a **random search with constraint checking** approach.
