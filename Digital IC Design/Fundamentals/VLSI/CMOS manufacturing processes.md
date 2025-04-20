# Manufacturing Processes for CMOS

## Introduction
- The CMOS process requires that both n-channel (NMOS) and p-channel (PMOS) transistors be built in the same silicon material.
- To accommodate both types of devices, special regions called **wells** must be created in which the semiconductor material is opposite to the type of the channel.
- A PMOS transistor has to be created in either an n-type substrate or an n-well, while an NMOS device resides in either a p-type substrate or a p-well.

## Manufacturing Stages
1. Wafer Production
2. Wafer Processes
3. Testing
4. Packing

## Wafer Production
1. Silicon is extracted from Silica sand, also known as quartz sand, white sand, or industrial sand.
   - Sand contains a high percentage of silicon in the form of SiO2.
2. Sand is heated until it melts, mixed with carbon to remove oxygen, and turned into a high-purity liquid of pure silicon.
3. The base material for the manufacturing process comes in the form of a single-crystalline rod or ingot.
4. The ingots are sliced into thinly sliced wafers with typical diameters between 4 and 12 inches and a thickness of at most 1 mm.
5. After slicing, the defect density of the base material is considered, and polishing machines are used to polish the rough surface of the wafer. The wafer is then cleaned to remove impurities.

## Photolithography
- Photolithography is a technique for selective masking.

### High-Level Steps
(A) Designer: Drawing "layer" patterns on a layout editor and sending the layout to the corresponding foundry.
(B) Foundry:
   - Masks generation from the layer patterns in the design database.
   - Photolithography process on each wafer, printing: transferring the mask pattern to the wafer surface.

1. Oxidation Growth (Layering)
   - Deposits a thin layer of SiO2 over the complete wafer by exposing it to a mixture of high-purity oxygen and hydrogen at approximately 1000°C.
   - The oxide is used as an insulation layer and forms transistor gates.
   - Types of oxidation:
     - Dry oxidation: carried out by oxygen gas and gaseous silicon, resulting in a thin oxide film.
     - Wet oxidation: carried out by water vapor, resulting in a thicker oxide.

2. Photoresist Coating
   - A light-sensitive polymer, similar to latex, is evenly applied while spinning the wafer to a thickness of approximately 1 mm.
   - This material is originally soluble in an organic solvent but has the property that the polymers...

   - Types of Photoresist:
     - Negative:
       (A) Before exposing to light: soluble in an organic solvent.
       (B) After exposing to light: insoluble.
     - Positive:
       (A) Before exposing to light: insoluble.
       (B) After exposing to light: soluble.

   - All below negative remain; all below positive are removed.

3. Stepper Exposure
   - A glass mask (or reticle), containing the patterns that need to be transferred to the silicon, is brought in close proximity to the wafer.
   - The mask is opaque in the regions that need to be processed and transparent in others.
   - The combination of mask and wafer is exposed to ultraviolet light.

4. Photoresist Development and Bake
   - Removing the photoresist layer, either positive or negative, by an acidic or basic solution.
   - After removing the oxide, the wafer (soft-baked) is heated at a lower temperature to harden the remaining photoresist.

5. Acid Etching (Wet Etching)
   - Material is selectively removed from areas of the wafer not covered by photoresist, such as removing the oxide that is not covered by photoresist.
   - This is accomplished through the use of many different types of acid, base, and caustic solutions depending on the material to be removed.

6. Spin, Rinse, and Dry
   - A special tool called SRD cleans the wafer with deionized water and dries it with nitrogen.
   - The microscopic scale of modern semiconductor devices means that even the smallest particle of dust or dirt can destroy the circuitry.

7. Various Process Steps
   - The exposed area can now be subjected to a wide range of process steps, such as ion implantation, plasma etching, or metal deposition.

8. Photoresist Removal (or Ashing)
   - A high-temperature plasma is used to selectively remove the remaining photoresist without damaging device layers.

## Discussing the Various Processes
- Many steps of the integrated circuit manufacturing process require a change in the dopant concentration of some parts of the material.
- The creation of the source and drain regions, well and substrate contacts, the doping of the polysilicon, and the adjustments of the device threshold.

### (1) Diffusion and Ion Implantation

(A) Diffusion Implantation
- The wafers are placed in a quartz tube embedded in a heated furnace.
- A gas containing the dopant is introduced into the tube.
- The high temperatures of the furnace, typically 900 to 1100°C, cause the dopants to diffuse into the exposed surface both vertically and horizontally.

(B) Ion Implantation
- Dopants are introduced as ions into the material.
- The ion implantation system directs and sweeps a beam of purified ions over the semiconductor surface.
- The acceleration of the ions determines how deep they will penetrate the material, while the beam current and the exposure time determine the dosage.

   - Problems of Ion Implantation
     - The most important one being lattice damage.
     - Nuclear collisions during high-energy implantation cause the displacement of substrate atoms, leading to material defects.

   - Solving the Problem (Annealing)
     - The wafer is heated to around 1000°C for 15 to 30 minutes, then allowed to cool slowly.
     - The heating step thermally vibrates the atoms, allowing the bonds to reform.

   - Surface Annealing
     - This involves exposing the substrate to an applied voltage that causes electrons to flow from the top downwards across the entire device.
     - This technique involves exposing the substrate to an external temperature that causes electron transfer from the crystal structure to the surface.
     - This method uses an electric field to heat up the crystalline structure of the substrate.

### (2) Deposition
- Deposition involves adding layers of material to the wafer, acting as buffers or insulating and conducting layers.

(Epitaxy)
- Silicon nitride (Si3N4) is used as a sacrificial buffer material during the formation of the field oxide and the introduction of stopper implants.
- This silicon nitride is deposited everywhere using a process called chemical vapor deposition (CVD).

- Polysilicon is used to increase the conductivity of the material.
- Metallization involves the deposition of metal layers by evaporation (e.g., interconnections) and uses physical vapor deposition (PVD).

### (3) Etching
- Etching is used to selectively remove material and create patterns.
- Dry etching is done using plasma.

### (4) Planarization
- To reliably deposit a layer of material onto the semiconductor surface, it is essential that the surface is approximately flat.
- A chemical-mechanical planarization (CMP) step is included before the deposition of an extra metal layer on top of the insulation layer of SiO2.





