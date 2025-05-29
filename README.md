# OpenWiringHarness
Towards a Free and complete wiring harness CAD

This poject want to create a set of tools to make Kicad (free electronics CAD) capable of handling wiring harness designs, in particular make it able to export a cutlist to then produce a real harness. The project could then be integrated with HarnessHelper to create an autoatic plugin.<br/> 

Actual state: <br/>
-HarnessHelper is usable  <br/>
-Extract_cutlist is a plugin exporting excel netlist of Kikad eeschema, to run the script:
```
python extract_cutlist.py target.kicad_sch
```
Todo  <br/>
-integrate lenghts in the export to build tha actual netlist  <br/>
-improve integration in Kicad
