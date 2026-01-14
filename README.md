# ALKF
Layout Generator Assignment
Overview

This project is a small program that automatically generates and visualizes multiple building layouts on a rectangular site while enforcing a set of geometric and proximity rules.
The goal is to explore different valid configurations and clearly visualize rule compliance.

Site & Building Setup
Site

Rectangular site: 200 m × 140 m

Coordinate system: (0,0) at bottom-left to (200,140) at top-right

Building Types
Building	Footprint
Tower A	30 m × 20 m
Tower B	20 m × 20 m
Central Plaza

Reserved open space: 40 m × 40 m

Located at the center of the site

No building footprints may overlap this area

Placement Rules Enforced

All buildings must lie completely inside the site.

Minimum distance between any two buildings: 15 m (edge-to-edge).

Minimum distance from any building to the site boundary: 10 m.

Neighbour-mix rule:
Every Tower A must have at least one Tower B within 60 m.

No building may overlap the central plaza.

Approach

A random search / heuristic placement strategy is used.

Buildings are placed iteratively while checking constraints.

Invalid placements are rejected automatically.

Multiple layouts are generated to explore different valid configurations.

Visual Output

Each generated layout includes:

Site boundary

Central plaza

Building footprints

Rule satisfaction status (shown in the plot title)

Multiple layouts are displayed as separate plots for easy comparison.

Colour Coding

Black outline → Site boundary

Light grey square → Central plaza

Red rectangles → Tower A buildings

Blue rectangles → Tower B buildings

This colour scheme makes it easy to distinguish building types and verify constraints visually.

Code Structure

layout_generator.py

Generates building layouts

Validates all rules

Visualizes layouts using plots

The same script handles generation, validation, and visualization.

Requirements

Python 3.x

Libraries:

numpy

matplotlib

Install dependencies using:

pip install numpy matplotlib

How to Run

Execute the following command:

python layout_generator.py


The program will automatically:

Generate multiple layout configurations

Validate rule compliance

Display visual outputs for each layout

Output

Multiple visual layouts

Clear indication of valid or violated rules

Easy comparison between different configurations

Possible Extensions

Genetic or evolutionary optimization

Interactive UI or sliders

Export layouts to CAD/DXF/JSON formats

Scoring-based optimization for density or open space

Author Notes

This solution prioritizes clarity, rule correctness, and visual interpretability, while remaining simple and extensible for future enhancements.
