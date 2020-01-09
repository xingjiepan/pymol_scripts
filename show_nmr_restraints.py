'''
Show NMR restraints from a .tbl file
'''

def show_nmr_restraints(restraint_file, long_range_only=True):
    with open(restraint_file, 'r') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if lines[i].strip().startswith('assi'):
            
            # Get all the restraint information.
            # Sometimes restraint is define across multiple lines
            
            total_line = ''
            total_line += lines[i]

            j = i + 1

            while j < len(lines):
                if lines[j].strip().startswith('assi'):
                    break
                total_line += lines[j]

                j += 1

            # Remove all the parenthesis

            clean_line = total_line.translate(None, '()').replace('#', '*')

            s_l = clean_line.split()
            print(s_l)

            res_ids = []
            atom_names = [] 

            for i in range(len(s_l)):
                if s_l[i] == 'resid':
                    res_ids.append(s_l[i + 1])
                if s_l[i] == 'name':
                    atom_names.append(s_l[i + 1])

            # Skip short range NOE

            seq_diff = int(res_ids[0]) - int(res_ids[1])

            if long_range_only:
                if seq_diff >= -3 and seq_diff <= 3:
                    continue

            # Show the restraint in pymol

            cmd.dist(None, 'i. ' + res_ids[0] + ' & n. ' + atom_names[0], 'i. ' + res_ids[1] + ' & n. ' + atom_names[1])

    cmd.set('dash_gap', 0.05)
    cmd.hide('labels')
    cmd.set('movie_delay', 1500)

cmd.extend("show_nmr_restraints", show_nmr_restraints)

