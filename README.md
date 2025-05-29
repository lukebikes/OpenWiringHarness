# OpenWiringHarness
Towards a Free and complete wiring harness CAD

This poject want to create a set of tools to make Kicad (free electronics CAD) capable of handling wiring harness designs, in particular make it able to export a cutlist to then produce a real harness. The project could then be integrated with HarnessHelper to create an autoatic plugin.

Actual state:
-HarnessHelper is usable
-Extract_cutlist is a plugin exporting excel netlist of Kikad eeschema, to run the script:
```
python extract_cutlist.py target.kicad_sch
```
Todo
-integrate lenghts in the export to build tha actual netlist
-improve integration in Kicad
