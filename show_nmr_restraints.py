'''
Show NMR restraints from a .tbl file
'''

def show_nmr_restraints(restraint_file):
    with open(restraint_file, 'r') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if lines[i].startswith('assign'):
            
            # Get all the restraint information.
            # Sometimes restraint is define across multiple lines
            
            total_line = ''
            total_line += lines[i]

            j = i + 1

            while j < len(lines):
                if lines[j].startswith('assign'):
                    break
                total_line += lines[j]

                j += 1

            # Remove all the parenthesis

            clean_line = total_line.translate(None, '()').replace('#', '*')

            s_l = clean_line.split()
            print(s_l)

            # Show the restraint in pymol

            cmd.dist(None, 'i. ' + s_l[2] + ' & n. ' + s_l[5], 'i. ' + s_l[7] + ' & n. ' + s_l[10])

    cmd.set('dash_gap', 0.05)
    cmd.hide('labels')
    cmd.set('movie_delay', 1500)

cmd.extend("show_nmr_restraints", show_nmr_restraints)

