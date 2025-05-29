import sexpdata
import pandas as pd
import itertools



def symbol_to_str(s):
    return s.value() if isinstance(s, sexpdata.Symbol) else str(s)

def parse_netlist_kicad9(filename):
    with open(filename, 'r') as f:
        data = sexpdata.loads(f.read())

    cutlist = []

    # Look for (nets ...)
    for item in data:
        if isinstance(item, list) and item and symbol_to_str(item[0]) == 'nets':
            for net in item[1:]:
                if not isinstance(net, list):
                    continue
                net_name = ''
                connections = []

                

                for part in net:
                    if isinstance(part, list) and part:
                        head = symbol_to_str(part[0])

                        if head == 'name':
                            net_name = symbol_to_str(part[1])
                        elif head == 'node':
                            ref = pin = None
                            for p in part[1:]:
                                if isinstance(p, list) and len(p) == 2:
                                    if symbol_to_str(p[0]) == 'ref':
                                        ref = symbol_to_str(p[1])
                                    elif symbol_to_str(p[0]) == 'pin':
                                        pin = symbol_to_str(p[1])
                            if ref and pin:
                                connections.append((ref, pin))

                # Only handle 2-pin nets for simple cutlist
                if len(connections) >= 2:
                    for from_conn, to_conn in itertools.combinations(connections, 2):
                        cutlist.append({
                          'From_Ref': from_conn[0],
                         'From_Pin': from_conn[1],
                         'To_Ref': to_conn[0],
                         'To_Pin': to_conn[1],
                         'Net_Name': net_name
                        })
                
    return cutlist

def export_to_excel(cutlist, output_file):
    df = pd.DataFrame(cutlist)
    df.to_excel(output_file, index=False)
    print(f"Cutlist exported to {output_file}")

# Example usage
input_netlist = 'Giacomo.net'  # Or your actual file
output_excel = 'cutlist.xlsx'

cutlist = parse_netlist_kicad9(input_netlist)
export_to_excel(cutlist, output_excel)
