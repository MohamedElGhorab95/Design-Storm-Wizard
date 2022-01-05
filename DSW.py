# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 01:57:00 2021

@author: M ElGhorab
"""

# =============================================================================
#                           Design Storm Wizard
# =============================================================================
print('# ============================================================================= #\n                       Welcome To Design Storm Wizard\nTool Developed by: Mohamed ElGhorab\n# ============================================================================= #')
### Prompt the User for input type (ty)
ty = input('Please specify your input type \nTotal Storm Depth or IDF Curve [SD/IDF]: ')
while ty != 'SD' and ty !='IDF' and ty !='sd' and ty !='idf':
    print('\nPlease Insert a valid type')
    ty = input('Total Storm Depth or IDF Curve [SD/IDF]: ')
# =============================================================================
#                             Frequency Storm 
# =============================================================================
if ty == 'IDF' or ty == 'idf':
    print('\n            initiating frequency storm generator...')
    IDF  = input('Please enter the file name [name.ext]: ')
    print('\nplease enter the time of peak rainfall \nDefault value is 50%\n')
    quad = input('Choose from(25, 33, 50, 67, 75): ')
    typ = 'Frequency'
    from functions.freq_strm import fr_strm
    DS = fr_strm(IDF,quad)
    print('\nPlease Check the output files for results ')    
    # export plot
    from functions.plt_hyetograph import hyt_plt
    fig = hyt_plt(DS,typ)
    # export txt file results
    from functions.exprt_strm import export_storm
    txt = export_storm(DS,typ)
# =============================================================================
#                               SCS Storm
# =============================================================================
if ty == 'SD'or ty =='sd':
    print('\n            initiating SCS storm generator...')
    depth = float(input('\nplease enter the maximum daily storm depth (mm): '))
    print('\nplease enter the required storm duration (hrs)\n ')
    durn = input('Choose from(0.5, 1, 2, 3, 4, 6, 12, 18, 24): ')
    typ = 'SCS II'
    from functions.SCSII import SCSII
    DS = SCSII(depth,durn)
    print('\nPlease Check the output files for results ')    
    # export plot
    from functions.plt_hyetograph import hyt_plt
    fig = hyt_plt(DS,typ)
    # export txt file results
    from functions.exprt_strm import export_storm
    txt = export_storm(DS,typ)
    