import numpy as np
import pandas as pd
import datetime
"""# NOTA PLACAS E CORREIOS

* v010. Há na maioria das esquinas da microárea placas com os nomes dos logradouros?

* v011. Os domicílios têm, predominantemente, acesso a serviços postais via:
"""

df['X_df'] = np.nan
df.loc[df['1_3_4']==1,'X_df'] = 6
df.loc[df['1_3_4']==2,'X_df'] = 4
df.loc[(df['1_3_4']==3)|
       (df['1_3_4']==4),'X_df'] = 3
df.loc[df['1_3_4']==5,'X_df'] = 2
df.loc[df['1_3_4']==6,'X_df'] = 1

df['Y_df'] = np.nan
df.loc[df['1_3_3']==1,'Y_df'] = 6
df.loc[df['1_3_3']==2,'Y_df'] = 1

df['NOTA PLACAS E CORREIOS'] = (df['X_df']*.5)+(df['Y_df']*.5)

"""# NOTA INFRA E MOBILIDADE

## Variáveis

*   v012. É possível circular internamente de moto?
* v013. O tempo médio a PÉ da via carroçável (automóveis) mais próxima até a microárea como um todo é:
* v014. Neste trajeto há trechos de média ou alta declividade?
* v015. É possível circular dentro da microárea de carro?
* v016. Nestas vias carroçáveis da microárea:
* v018. Há pavimentação nestas vias carroçáveis da microárea?
* v019. A maior parte das vias carroçáveis da microárea está com a pavimentação de acordo:
* v020. Há também uma minoria de vias carroçáveis de acordo com algum outro padrão?
* v021. Nos trechos de vias carroçáveis da microárea há calçadas para pedestres?
* v022. As calçadas para pedestres estão:
* V023. As condições das calçadas permitem uma boa caminhabilidade das pessoas?
* v024. Quais são os principais obstáculos encontrados nas calçadas da comunidade que dificultam a caminhabilidade das pessoas?
* v025. Qual o nível de arborização das calçadas?
* v026. Há pavimentação nas vielas, becos, escadarias e passarelas?
* v027. A maior parte das vielas, becos, escadarias e passarelas da microárea está com a pavimentação de acordo com:
* v028. Há também uma minoria de vielas, becos, escadarias e passarelas de acordo com algum outro padrão?

## Código
"""

df['Pm_IM'] = np.nan
df.loc[df['2_1_1']==1,'Pm_IM'] = 1
df.loc[df['2_1_1']==2,'Pm_IM'] = .75
df.loc[df['2_1_1']==3,'Pm_IM'] = .25
df.loc[(df['2_1_1']==4)|
       (df['2_1_1']==0),'Pm_IM'] = 0

df['Pc_IM'] = np.nan
df.loc[df['2_1_4']==1,'Pc_IM'] = 1
df.loc[df['2_1_4']==2,'Pc_IM'] = .75
df.loc[df['2_1_4']==3,'Pc_IM'] = .25
df.loc[(df['2_1_4']==4)|
       (df['2_1_4']==0),'Pc_IM'] = 0

df['Pp_IM'] = 1 - df['Pm_IM']

df['K_IM'] = np.nan
df.loc[df['2_1_5']==1,'K_IM'] = 0
df.loc[df['2_1_5']==2,'K_IM'] = .3
df.loc[(df['2_1_5']!=1)&
      (df['2_1_5']!=2),'K_IM'] = 0

df['X_IM'] = (df['Pc_IM'] * 6 + (df['Pm_IM'] - df['Pc_IM']) * 3 + df['Pp_IM'] * 1) - df['K_IM']

df['Y_IM'] = np.nan
df.loc[(df['2_1_2']==1)&
      (df['2_1_3']==3),'Y_IM'] = 10
df.loc[(df['2_1_2']==1)&
      (df['2_1_3']==2),'Y_IM'] = 10
df.loc[(df['2_1_2']==1)&
      (df['2_1_3']==1),'Y_IM'] = 10
df.loc[(df['2_1_2']==2)&
      (df['2_1_3']==3),'Y_IM'] = 9
df.loc[(df['2_1_2']==2)&
      (df['2_1_3']==2),'Y_IM'] = 8
df.loc[(df['2_1_2']==2)&
      (df['2_1_3']==1),'Y_IM'] = 7
df.loc[(df['2_1_2']==3)&
      (df['2_1_3']==3),'Y_IM'] = 6
df.loc[(df['2_1_2']==3)&
      (df['2_1_3']==2),'Y_IM'] = 5
df.loc[(df['2_1_2']==3)&
      (df['2_1_3']==1),'Y_IM'] = 4
df.loc[(df['2_1_2']==4)&
      (df['2_1_3']==3),'Y_IM'] = 3
df.loc[(df['2_1_2']==4)&
      (df['2_1_3']==2),'Y_IM'] = 2
df.loc[(df['2_1_2']==4)&
      (df['2_1_3']==1),'Y_IM'] = 1

df['Y_IM'] = (df['Y_IM']/10)*6

N1_IM = 1

df['S1_IM'] = np.nan

df.loc[((df['2_1_6']<5)&(df['2_1_6']>0))&
      ((df['2_1_7']==1)&(df['2_1_8']==2)),'S1_IM'] = 6 * .7 + 4 * .3
df.loc[((df['2_1_6']<5)&(df['2_1_6']>0))&
      ((df['2_1_7']==1)&(df['2_1_8']==3)),'S1_IM'] = 6 * .7 + 2 * .3
df.loc[((df['2_1_6']<5)&(df['2_1_6']>0))&
      ((df['2_1_7']==2)&(df['2_1_8']==1)),'S1_IM'] = 4 * .7 + 6 * .3
df.loc[((df['2_1_6']<5)&(df['2_1_6']>0))&
      ((df['2_1_7']==2)&(df['2_1_8']==3)),'S1_IM'] = 4 * .7 + 2 * .3
df.loc[((df['2_1_6']<5)&(df['2_1_6']>0))&
      ((df['2_1_7']==3)&(df['2_1_8']==1)),'S1_IM'] = 2 * .7 + 6 * .3
df.loc[((df['2_1_6']<5)&(df['2_1_6']>0))&
      ((df['2_1_7']==3)&(df['2_1_8']==2)),'S1_IM'] = 2 * .7 + 4 * .3
df.loc[((df['2_1_6']<5)&(df['2_1_6']>0))&
      ((df['2_1_7']==1)&(df['2_1_8']==4)),'S1_IM'] = 6
df.loc[((df['2_1_6']<5)&(df['2_1_6']>0))&
      ((df['2_1_7']==2)&(df['2_1_8']==4)),'S1_IM'] = 4
df.loc[((df['2_1_6']<5)&(df['2_1_6']>0))&
      ((df['2_1_7']==3)&(df['2_1_8']==4)),'S1_IM'] = 2
df.loc[(df['2_1_6']==5),'S1_IM'] = 1
df.loc[(df['2_1_6']==0),'S1_IM'] = np.nan

df['P1_IM'] = np.nan
df.loc[df['2_1_6']==1,'P1_IM'] = 1
df.loc[df['2_1_6']==2,'P1_IM'] = .75
df.loc[df['2_1_6']==3,'P1_IM'] = .5
df.loc[df['2_1_6']==4,'P1_IM'] = .25
df.loc[df['2_1_6']==5,'P1_IM'] = 0

df['Z1_IM'] = np.nan
df.loc[(df['S1_IM'].isnull())&
      (df['P1_IM'].isnull()),'Z1_IM'] = 0
df.loc[(~df['S1_IM'].isnull())|
      (~df['P1_IM'].isnull()),'Z1_IM'] = ((df['S1_IM'] * df['P1_IM']) + (N1_IM * (1 - df['P1_IM']) * 3)) / (df['P1_IM'] * 1 +  (1 - df['P1_IM']) * 3 )

N2_IM = 1

df['S2_IM'] = np.nan

df.loc[((df['2_1_11']<5)&(df['2_1_11']>0))&
      ((df['2_1_12']==1)&(df['2_1_13']==2)),'S2_IM'] = 6 * .7 + 4 * .3
df.loc[((df['2_1_11']<5)&(df['2_1_11']>0))&
      ((df['2_1_12']==1)&(df['2_1_13']==3)),'S2_IM'] = 6 * .7 + 2 * .3
df.loc[((df['2_1_11']<5)&(df['2_1_11']>0))&
      ((df['2_1_12']==2)&(df['2_1_13']==1)),'S2_IM'] = 4 * .7 + 6 * .3
df.loc[((df['2_1_11']<5)&(df['2_1_11']>0))&
      ((df['2_1_12']==2)&(df['2_1_13']==3)),'S2_IM'] = 4 * .7 + 2 * .3
df.loc[((df['2_1_11']<5)&(df['2_1_11']>0))&
      ((df['2_1_12']==3)&(df['2_1_13']==1)),'S2_IM'] = 2 * .7 + 6 * .3
df.loc[((df['2_1_11']<5)&(df['2_1_11']>0))&
      ((df['2_1_12']==3)&(df['2_1_13']==2)),'S2_IM'] = 2 * .7 + 4 * .3
df.loc[((df['2_1_11']<5)&(df['2_1_11']>0))&
      ((df['2_1_12']==1)&(df['2_1_13']==4)),'S2_IM'] = 6
df.loc[((df['2_1_11']<5)&(df['2_1_11']>0))&
      ((df['2_1_12']==2)&(df['2_1_13']==4)),'S2_IM'] = 4
df.loc[((df['2_1_11']<5)&(df['2_1_11']>0))&
      ((df['2_1_12']==3)&(df['2_1_13']==4)),'S2_IM'] = 2
df.loc[(df['2_1_11']==5),'S2_IM'] = 1
df.loc[(df['2_1_11']==6),'S2_IM'] = np.nan

df['P2_IM'] = np.nan
df.loc[df['2_1_11']==1,'P2_IM'] = 1
df.loc[df['2_1_11']==2,'P2_IM'] = .75
df.loc[df['2_1_11']==3,'P2_IM'] = .5
df.loc[df['2_1_11']==4,'P2_IM'] = .25
df.loc[df['2_1_11']==5,'P2_IM'] = 0

df['Z2_IM'] = np.nan
df.loc[(df['S2_IM'].isnull())&
      (df['P2_IM'].isnull()),'Z2_IM'] = 0
df.loc[(~df['S2_IM'].isnull())|
      (~df['P2_IM'].isnull()),'Z2_IM'] = ((df['S2_IM'] * df['P2_IM']) + (N2_IM * (1 - df['P2_IM']) * 3)) / (df['P2_IM'] * 1 +  (1 - df['P2_IM']) * 3 )

df['W1_IM'] = np.nan
df.loc[(df['2_1_4']==1)&
      (df['2_1_11']==6),'W1_IM'] = 1
df.loc[(df['2_1_4']==1)&
      (df['2_1_11']!=6),'W1_IM'] = .75
df.loc[(df['2_1_4']==2),'W1_IM'] = .5
df.loc[(df['2_1_4']==3),'W1_IM'] = .25
df.loc[(df['2_1_4']!=1)&
       (df['2_1_4']!=2)&
       (df['2_1_4']!=3),'W1_IM'] = 0

df['W2_IM'] = 1 - df['W1_IM']

df['Z_IM'] = (df['Z1_IM'] * df['W1_IM']) + (df['Z2_IM'] * df['W2_IM'])

df['NOTA INFRA PARA MOBILIDADE'] = df['X_IM'] * .2 + df['Y_IM'] * .4 + df['Z_IM'] * .4

"""# NOTA TRANSPORTE

#### NOTA PONTO MAIS PERTO
"""

df['Dx1_TR'] = np.nan
df.loc[df['2_2_1']==1,'Dx1_TR'] = 1
df.loc[df['2_2_1']==2,'Dx1_TR'] = .95
df.loc[df['2_2_1']==3,'Dx1_TR'] = .9
df.loc[df['2_2_1']==4,'Dx1_TR'] = .75
df.loc[df['2_2_1']==5,'Dx1_TR'] = .5
df.loc[df['2_2_1']==6,'Dx1_TR'] = .25

df['Qx1_TR'] = 0
df.loc[(df['2_2_4']==1)&
      (df['2_2_3']==1),'Qx1_TR'] = 1
df.loc[(df['2_2_4']==1)&
      (df['2_2_3']==2),'Qx1_TR'] = .9
df.loc[(df['2_2_4']==2)&
      (df['2_2_3']==1),'Qx1_TR'] = .7
df.loc[(df['2_2_4']==2)&
      (df['2_2_3']==2),'Qx1_TR'] = .5
df.loc[(df['2_2_4']==3)&
      (df['2_2_3']==1),'Qx1_TR'] = .3
df.loc[(df['2_2_4']==3)&
      (df['2_2_3']==2),'Qx1_TR'] = .1

df['X_TR'] = 6 * df['Dx1_TR'] * df['Qx1_TR']

'''
df['K1_TR'] = np.nan
df.loc[df['2_2_8']!=7,'K1_TR'] = 6

df['Dk_TR'] = np.nan
df.loc[df['2_2_8']==1,'Dk_TR'] = 1
df.loc[df['2_2_8']==2,'Dk_TR'] = .95
df.loc[df['2_2_8']==3,'Dk_TR'] = .9
df.loc[df['2_2_8']==4,'Dk_TR'] = .75
df.loc[df['2_2_8']==5,'Dk_TR'] = .5
df.loc[df['2_2_8']==6,'Dk_TR'] = .25

df['Qk_TR'] = df['Qx1_TR']

df['Gk_TR'] = np.nan
df.loc[df['2_2_9']==1,'Gk_TR'] = .75
df.loc[df['2_2_9']==2,'Gk_TR'] = .5
df.loc[df['2_2_9']==3,'Gk_TR'] = .25

df['K_TR'] = np.nan
df.loc[df['K1_TR']==6,
       'K_TR'] = 6 * df['Dk_TR'] * df['Qk_TR'] * df['Gk_TR']
'''

df['W1_TR'] = np.nan
df.loc[df['2_2_5']!=7,'W1_TR'] = 6

df['Dw_TR'] = np.nan
df.loc[df['2_2_5']==1,'Dw_TR'] = 1
df.loc[df['2_2_5']==2,'Dw_TR'] = .95
df.loc[df['2_2_5']==3,'Dw_TR'] = .9
df.loc[df['2_2_5']==4,'Dw_TR'] = .75
df.loc[df['2_2_5']==5,'Dw_TR'] = .5
df.loc[df['2_2_5']==6,'Dw_TR'] = .25

df['Qw_TR'] = df['Qx1_TR']

df['Gw_TR'] = np.nan
df.loc[df['2_2_6']==1,'Gw_TR'] = .5
df.loc[df['2_2_6']==2,'Gw_TR'] = .25
df.loc[df['2_2_6']==3,'Gw_TR'] = .125

df['W_TR'] = np.nan
df.loc[df['W1_TR']==6,
       'W_TR'] = 6 * df['Dw_TR'] * df['Qw_TR'] * df['Gw_TR']

df['Z1_TR'] = 6
df.loc[(df['2_2_7']==7)&
       (df['2_2_7']>0),'Z1_TR'] = np.nan

df['Dz_TR'] = np.nan
df.loc[df['2_2_7']==1,'Dz_TR'] = 1
df.loc[df['2_2_7']==2,'Dz_TR'] = .95
df.loc[df['2_2_7']==3,'Dz_TR'] = .9
df.loc[df['2_2_7']==4,'Dz_TR'] = .75
df.loc[df['2_2_7']==5,'Dz_TR'] = .5
df.loc[df['2_2_7']==6,'Dz_TR'] = .25
df.loc[df['2_2_7']==0,'Dz_TR'] = 0

df['Qz_TR'] = df['Qx1_TR']

df['Gz_TR'] = .125

df['Z_TR'] = np.nan
df.loc[df['Z1_TR']==6,
        'Z_TR'] = 6 * df['Dz_TR'] * df['Qz_TR'] * df['Gz_TR']

'''
df['Y1_TR'] = np.nan
df.loc[~df['K_TR'].isnull(),
       'Y1_TR'] = df['X_TR'] * (1 - df['Gk_TR']) + df['K_TR']
'''

df['Y2_TR'] = np.nan
df.loc[~df['W_TR'].isnull(),
       'Y2_TR'] = df['X_TR'] * (1 - df['Gw_TR']) + df['W_TR']

df['Y3_TR'] = np.nan
df.loc[~df['Z_TR'].isnull(),
       'Y3_TR'] = df['X_TR'] * (1 - df['Gz_TR']) + df['Z_TR']

df['NOTA PERTO'] = df[['X_TR',
                       #'Y1_TR',
                       'Y2_TR',
                       'Y3_TR']].max(axis=1)

"""#### NOTA PONTO MAIS UTILIZADO"""

df['M1_TR'] = 6

df['Dm1_TR'] = np.nan
df.loc[df['2_2_10']==1,'Dm1_TR'] = 1
df.loc[df['2_2_10']==2,'Dm1_TR'] = .95
df.loc[df['2_2_10']==3,'Dm1_TR'] = .9
df.loc[df['2_2_10']==4,'Dm1_TR'] = .75
df.loc[df['2_2_10']==5,'Dm1_TR'] = .5
df.loc[df['2_2_10']==6,'Dm1_TR'] = .25

df['Qm1_TR'] = np.nan
df.loc[(df['2_2_13']==1)&
      (df['2_2_12']==1),'Qm1_TR'] = 1
df.loc[(df['2_2_13']==1)&
      (df['2_2_12']==2),'Qm1_TR'] = .9
df.loc[(df['2_2_13']==2)&
      (df['2_2_12']==1),'Qm1_TR'] = .7
df.loc[(df['2_2_13']==2)&
      (df['2_2_12']==2),'Qm1_TR'] = .5
df.loc[(df['2_2_13']==3)&
      (df['2_2_12']==1),'Qm1_TR'] = .3
df.loc[(df['2_2_13']==3)&
      (df['2_2_12']==2),'Qm1_TR'] = .1

df['M_TR'] = np.nan
df.loc[(~df['Dm1_TR'].isnull())|
      (~df['Qm1_TR'].isnull()),'M_TR'] = df['M1_TR'] * df['Dm1_TR'] * df['Qm1_TR']

'''
df['P1_TR'] = np.nan
df.loc[(df['2_2_17']<7)&
       (df['2_2_17']>0),'P1_TR'] = 6

df['Dp_TR'] = np.nan
df.loc[df['2_2_17']==1,'Dp_TR'] = 1
df.loc[df['2_2_17']==2,'Dp_TR'] = .95
df.loc[df['2_2_17']==3,'Dp_TR'] = .9
df.loc[df['2_2_17']==4,'Dp_TR'] = .75
df.loc[df['2_2_17']==5,'Dp_TR'] = .5
df.loc[df['2_2_17']==6,'Dp_TR'] = .25

df['Qp_TR'] = np.nan
df.loc[(df['2_2_15']==1)&
      (df['2_2_14']==1),'Qp_TR'] = 1
df.loc[(df['2_2_15']==1)&
      (df['2_2_14']==2),'Qp_TR'] = .9
df.loc[(df['2_2_15']==2)&
      (df['2_2_14']==1),'Qp_TR'] = .7
df.loc[(df['2_2_15']==2)&
      (df['2_2_14']==2),'Qp_TR'] = .5
df.loc[(df['2_2_15']==3)&
      (df['2_2_14']==1),'Qp_TR'] = .3
df.loc[(df['2_2_15']==3)&
      (df['2_2_14']==2),'Qp_TR'] = .1

df['Gp_TR'] = np.nan
df.loc[df['2_2_18']==1,'Gp_TR'] = .75
df.loc[df['2_2_18']==2,'Gp_TR'] = .5
df.loc[df['2_2_18']==3,'Gp_TR'] = .25

df['P_TR'] = np.nan
df.loc[df['2_2_17']!=7,
       'P_TR'] = df['P1_TR'] * df['Dp_TR'] * df['Qp_TR'] * df['Gp_TR']
'''

df['R1_TR'] = np.nan
df.loc[(df['2_2_14']<7)&
       (df['2_2_14']>0),'R1_TR'] = 6

df['Dr_TR'] = np.nan
df.loc[df['2_2_14']==1,'Dr_TR'] = 1
df.loc[df['2_2_14']==2,'Dr_TR'] = .95
df.loc[df['2_2_14']==3,'Dr_TR'] = .9
df.loc[df['2_2_14']==4,'Dr_TR'] = .75
df.loc[df['2_2_14']==5,'Dr_TR'] = .5
df.loc[df['2_2_14']==6,'Dr_TR'] = .25

df['Qr_TR'] = np.nan
df.loc[(df['2_2_13']==1)&
      (df['2_2_12']==1),'Qr_TR'] = 1
df.loc[(df['2_2_13']==1)&
      (df['2_2_12']==2),'Qr_TR'] = .9
df.loc[(df['2_2_13']==2)&
      (df['2_2_12']==1),'Qr_TR'] = .7
df.loc[(df['2_2_13']==2)&
      (df['2_2_12']==2),'Qr_TR'] = .5
df.loc[(df['2_2_13']==3)&
      (df['2_2_12']==1),'Qr_TR'] = .3
df.loc[(df['2_2_13']==3)&
      (df['2_2_12']==2),'Qr_TR'] = .1

df['Gr_TR'] = np.nan
df.loc[df['2_2_15']==1,'Gr_TR'] = .5
df.loc[df['2_2_15']==2,'Gr_TR'] = .25
df.loc[df['2_2_15']==3,'Gr_TR'] = .125

df['R_TR'] = np.nan
df.loc[df['2_2_14']!=7,
      'R_TR'] = df['R1_TR'] * df['Dr_TR'] * df['Qr_TR'] * df['Gr_TR']

df['S1_TR'] = np.nan
df.loc[(df['2_2_16']<7)&
       (df['2_2_16']>0),'S1_TR'] = 6

df['Ds_TR'] = np.nan
df.loc[df['2_2_16']==1,'Ds_TR'] = 1
df.loc[df['2_2_16']==2,'Ds_TR'] = .95
df.loc[df['2_2_16']==3,'Ds_TR'] = .9
df.loc[df['2_2_16']==4,'Ds_TR'] = .75
df.loc[df['2_2_16']==5,'Ds_TR'] = .5
df.loc[df['2_2_16']==6,'Ds_TR'] = .25

df['Qs_TR'] = np.nan
df.loc[(df['2_2_13']==1)&
      (df['2_2_12']==1),'Qs_TR'] = 1
df.loc[(df['2_2_13']==1)&
      (df['2_2_12']==2),'Qs_TR'] = .9
df.loc[(df['2_2_13']==2)&
      (df['2_2_12']==1),'Qs_TR'] = .7
df.loc[(df['2_2_13']==2)&
      (df['2_2_12']==2),'Qs_TR'] = .5
df.loc[(df['2_2_13']==3)&
      (df['2_2_12']==1),'Qs_TR'] = .3
df.loc[(df['2_2_13']==3)&
      (df['2_2_12']==2),'Qs_TR'] = .1

df['Gs_TR'] = .125

df['S_TR'] = np.nan
df.loc[((~df['Ds_TR'].isnull())|
      (~df['Qs_TR'].isnull()))&
       (df['2_2_16']!=7),
        'S_TR'] = df['S1_TR'] * df['Ds_TR'] * df['Qs_TR'] * df['Gs_TR']

'''
df['N1_TR'] = np.nan
df.loc[~df['P_TR'].isnull(),
       'N1_TR'] = df['M_TR'] * (1 - df['Gp_TR']) + df['P_TR']
'''

df['N2_TR'] = np.nan
df.loc[~df['R_TR'].isnull(),
       'N2_TR'] = df['M_TR'] * (1 - df['Gr_TR']) + df['R_TR']

df['N3_TR'] = np.nan
df.loc[~df['S_TR'].isnull(),
       'N3_TR'] = df['M_TR'] * (1 - df['Gs_TR']) + df['S_TR']

df['NOTA UTILIZADO'] = np.nan
df.loc[~df['M_TR'].isnull(),
       'NOTA UTILIZADO'] = df[['M_TR',
                               #'N1_TR',
                               'N2_TR',
                               'N3_TR']].max(axis=1)

df['NOTA TRANSPORTE'] = np.nan
df.loc[df['NOTA UTILIZADO'].isnull(),
      'NOTA TRANSPORTE'] = df['NOTA PERTO']
df.loc[df['NOTA PERTO']>=df['NOTA UTILIZADO'],
      'NOTA TRANSPORTE'] = df['NOTA PERTO']
df.loc[df['NOTA PERTO']<df['NOTA UTILIZADO'],
      'NOTA TRANSPORTE'] = df['NOTA UTILIZADO'] + .1 * df['NOTA PERTO']
df.loc[df['NOTA TRANSPORTE']>6,'NOTA TRANSPORTE'] = 6

"""# NOTA MORADIA"""

df['X_MO'] = np.nan
df.loc[(df['3_1_1']==1)|
      (df['3_1_1']==2),'X_MO'] = 6
df.loc[(df['3_1_1']!=1)&
      (df['3_1_1']!=2),'X_MO'] = 0

df['Y_MO'] = np.nan
df.loc[(df['3_1_1']==3)|
      (df['3_1_1']==4),'Y_MO'] = 1
df.loc[(df['3_1_1']!=3)|
      (df['3_1_1']!=4),'Y_MO'] = 0

df['R_MO'] = np.nan
df.loc[(df['3_1_1']==1)&
       (df['X_MO']==6),'R_MO'] = 6
df.loc[(df['3_1_1']==2)&
       (df['X_MO']==6),'R_MO'] = 1
df.loc[((df['3_1_1']!=1)&(df['3_1_1']!=2))|
       (df['X_MO']!=6),'R_MO'] = 0

df['X1_X2_Y_MO'] = np.nan
df.loc[(df['R_MO']>0),'X1_X2_Y_MO'] = 6 * .5 + df['R_MO'] * .5
df.loc[(df['R_MO']==0),'X1_X2_Y_MO'] = 1

df['P1_MO'] = np.nan
df.loc[(df['3_1_1']!=1)&
       (df['3_1_2']!=1)&
       (df['3_1_3']!=1),'P1_MO'] = 0
df.loc[(df['3_1_3']==1),'P1_MO'] = .1
df.loc[(df['3_1_2']==1),'P1_MO'] = .3
df.loc[(df['3_1_1']==1)&
       (df['3_1_2']!=5)&
       (df['3_1_3']!=5),'P1_MO'] = .6
df.loc[(df['3_1_1']==1)&
       (df['3_1_2']!=5)&
       (df['3_1_3']==5),'P1_MO'] = .7
df.loc[(df['3_1_1']==1)&
       (df['3_1_2']==5)&
       (df['3_1_3']!=5),'P1_MO'] = .9
df.loc[(df['3_1_1']==1)&
       (df['3_1_2']==5)&
       (df['3_1_3']==5),'P1_MO'] = 1

df['P2_MO'] = np.nan
df.loc[(df['3_1_1']!=2)&
       (df['3_1_2']!=2)&
       (df['3_1_3']!=2),'P2_MO'] = 0
df.loc[(df['3_1_3']==2),'P2_MO'] = .1
df.loc[(df['3_1_2']==2),'P2_MO'] = .3
df.loc[(df['3_1_1']==2)&
       (df['3_1_2']!=5)&
       (df['3_1_3']!=5),'P2_MO'] = .6
df.loc[(df['3_1_1']==2)&
       (df['3_1_2']!=5)&
       (df['3_1_3']==5),'P2_MO'] = .7
df.loc[(df['3_1_1']==2)&
       (df['3_1_2']==5)&
       (df['3_1_3']!=5),'P2_MO'] = .9
df.loc[(df['3_1_1']==2)&
       (df['3_1_2']==5)&
       (df['3_1_3']==5),'P2_MO'] = 1

df['P3_MO'] = np.nan
df.loc[(df['3_1_1']!=3)&(df['3_1_1']!=4)&
       (df['3_1_2']!=3)&(df['3_1_2']!=4)&
       (df['3_1_3']!=3)&(df['3_1_3']!=4),'P3_MO'] = 0
df.loc[(df['3_1_3']==3)|(df['3_1_3']==4),'P3_MO'] = .1
df.loc[(df['3_1_2']==3)|(df['3_1_2']==4),'P3_MO'] = .3
df.loc[((df['3_1_1']==3)|(df['3_1_1']==4))&
       (df['3_1_2']!=5)&
       (df['3_1_3']!=5),'P3_MO'] = .6
df.loc[((df['3_1_1']==3)|(df['3_1_1']==4))&
       (df['3_1_2']!=5)&
       (df['3_1_3']==5),'P3_MO'] = .7
df.loc[((df['3_1_1']==3)|(df['3_1_1']==4))&
       (df['3_1_2']==5)&
       (df['3_1_3']!=5),'P3_MO'] = .9
df.loc[((df['3_1_1']==3)|(df['3_1_1']==4))&
       (df['3_1_2']==5)&
       (df['3_1_3']==5),'P3_MO'] = 1

df['N_MO'] = (6 * df['P1_MO'] + 3.5 * df['P2_MO'] + 1 * df['P3_MO'] * 5) / (df['P1_MO'] + df['P2_MO'] + df['P3_MO'] * 5)

df['D_MO'] = np.nan
df.loc[df['3_1_5']==1,'D_MO'] = 0
df.loc[df['3_1_5']==2,'D_MO'] = .4
df.loc[df['3_1_5']==3,'D_MO'] = .8

df['NOTA MORADIA'] = df['N_MO'] - df['D_MO']

"""# NOTA ÁGUA"""

df['X1M_AG'] = np.nan
df.loc[(df['4_1_1']==1)&
      (df['4_1_4']==1),'X1M_AG'] = 9
df.loc[(df['4_1_1']==1)&
      (df['4_1_4']==2),'X1M_AG'] = 8
df.loc[(df['4_1_1']==1)&
      (df['4_1_4']==3),'X1M_AG'] = 7
df.loc[(df['4_1_1']==1)&
      (df['4_1_4']==4),'X1M_AG'] = 6

df.loc[(df['4_1_1']==2)&
      (df['4_1_4']==1),'X1M_AG'] = 5
df.loc[(df['4_1_1']==2)&
      (df['4_1_4']==2),'X1M_AG'] = 4
df.loc[(df['4_1_1']==2)&
      (df['4_1_4']==3),'X1M_AG'] = 3
df.loc[(df['4_1_1']==2)&
      (df['4_1_4']==4),'X1M_AG'] = 2

df.loc[(df['4_1_1']==3),'X1M_AG'] = 1

df['X1M_AG'] = (df['X1M_AG']/9) * 6

df['X1m_AG'] = np.nan
df.loc[(df['4_1_2']==1)&
      (df['4_1_4']==1),'X1m_AG'] = 9
df.loc[(df['4_1_2']==1)&
      (df['4_1_4']==2),'X1m_AG'] = 8
df.loc[(df['4_1_2']==1)&
      (df['4_1_4']==3),'X1m_AG'] = 7
df.loc[(df['4_1_2']==1)&
      (df['4_1_4']==4),'X1m_AG'] = 6

df.loc[(df['4_1_2']==2)&
      (df['4_1_4']==1),'X1m_AG'] = 5
df.loc[(df['4_1_2']==2)&
      (df['4_1_4']==2),'X1m_AG'] = 4
df.loc[(df['4_1_2']==2)&
      (df['4_1_4']==3),'X1m_AG'] = 3
df.loc[(df['4_1_2']==2)&
      (df['4_1_4']==4),'X1m_AG'] = 2

df.loc[(df['4_1_2']==3),'X1m_AG'] = 1

df.loc[(df['4_1_2']==4),'X1m_AG'] = 0

df['X1m_AG'] = (df['X1m_AG']/9) * 6

df['X2M_AG'] = np.nan
df.loc[(df['4_1_1']!=1),'X2M_AG'] = df['X1M_AG']
df.loc[(df['4_1_1']==1)&
       (df['4_1_3']==2),'X2M_AG'] = df['X1M_AG'] - .5
df.loc[(df['4_1_1']==1)&
       (df['4_1_3']==1),'X2M_AG'] = df['X1M_AG'] - 1
df.loc[(df['4_1_1']==1)&
       ((df['4_1_3']==3)|(df['4_1_3']==0)),'X2M_AG'] = df['X1M_AG']

df['X2m_AG'] = np.nan
df.loc[(df['4_1_2']!=1),'X2m_AG'] = df['X1m_AG']
df.loc[(df['4_1_2']==1)&
       (df['4_1_3']==2),'X2m_AG'] = df['X1m_AG'] - .5
df.loc[(df['4_1_2']==1)&
       (df['4_1_3']==1),'X2m_AG'] = df['X1m_AG'] - 1
df.loc[(df['4_1_2']==1)&
       ((df['4_1_3']==3)|(df['4_1_3']==0)),'X2m_AG'] = df['X1m_AG']

df['X2_AG'] = df['X2M_AG'] * .7 + df['X2m_AG'] * .3

df['X3iM_AG'] = np.nan
df.loc[(df['4_1_1']!=3)&
       (df['4_1_5']==1),'X3iM_AG'] = df['X2M_AG'] * 1
df.loc[(df['4_1_1']!=3)&
       (df['4_1_5']==2),'X3iM_AG'] = df['X2M_AG'] * .9
df.loc[(df['4_1_1']!=3)&
       (df['4_1_5']==3),'X3iM_AG'] = df['X2M_AG'] * .6
df.loc[(df['4_1_1']!=3)&
       (df['4_1_5']==4),'X3iM_AG'] = df['X2M_AG'] * .3
df.loc[df['4_1_1']==3,'X3iM_AG'] = df['X2M_AG']

df['X3iiM_AG'] = np.nan
df.loc[(df['4_1_1']!=3)&
       (df['4_1_6']==1),'X3iiM_AG'] = df['X2M_AG']
df.loc[(df['4_1_1']!=3)&
       (df['4_1_6']==2),'X3iiM_AG'] = df['X2M_AG'] * .9
df.loc[(df['4_1_1']!=3)&
       (df['4_1_6']==3),'X3iiM_AG'] = df['X2M_AG'] * .6
df.loc[(df['4_1_1']!=3)&
       (df['4_1_6']==4),'X3iiM_AG'] = df['X2M_AG'] * .3
df.loc[df['4_1_1']==3,'X3iiM_AG'] = df['X2M_AG']

df['X3M_AG'] = df['X3iM_AG'] * .6 + df['X3iiM_AG'] * .4

df['X3im_AG'] = np.nan
df.loc[((df['4_1_2']==1)|(df['4_1_2']==2))&
       (df['4_1_5']==1),'X3im_AG'] = df['X2m_AG']
df.loc[((df['4_1_2']==1)|(df['4_1_2']==2))&
       (df['4_1_5']==2),'X3im_AG'] = df['X2m_AG'] * .9
df.loc[((df['4_1_2']==1)|(df['4_1_2']==2))&
       (df['4_1_5']==3),'X3im_AG'] = df['X2m_AG'] * .6
df.loc[((df['4_1_2']==1)|(df['4_1_2']==2))&
       (df['4_1_5']==4),'X3im_AG'] = df['X2m_AG'] * .3
df.loc[(df['4_1_2']!=1)&(df['4_1_2']!=2),'X3im_AG'] = df['X2m_AG']

df['X3iim_AG'] = np.nan
df.loc[((df['4_1_2']==1)|(df['4_1_2']==2))&
       (df['4_1_6']==1),'X3iim_AG'] = df['X2m_AG']
df.loc[((df['4_1_2']==1)|(df['4_1_2']==2))&
       (df['4_1_6']==2),'X3iim_AG'] = df['X2m_AG'] * .9
df.loc[((df['4_1_2']==1)|(df['4_1_2']==2))&
       (df['4_1_6']==3),'X3iim_AG'] = df['X2m_AG'] * .6
df.loc[((df['4_1_2']==1)|(df['4_1_2']==2))&
       (df['4_1_6']==4),'X3iim_AG'] = df['X2m_AG'] * .3
df.loc[(df['4_1_2']!=1)&(df['4_1_2']!=2),'X3iim_AG'] = df['X2m_AG']

df['X3m_AG'] = df['X3im_AG'] * .6 + df['X3iim_AG'] * .4

df['X4M_AG'] = np.nan
df.loc[(df['4_1_1']!=3)&(df['4_1_7']==2),'X4M_AG'] = df['X3M_AG'] * (2 / 3)
df.loc[(df['4_1_1']==3)|(df['4_1_7']!=2),'X4M_AG'] = df['X3M_AG']

df['X4m_AG'] = np.nan
df.loc[((df['4_1_2']==1)|(df['4_1_2']==2))&
       (df['4_1_7']==2),'X4m_AG'] = df['X3m_AG'] * (2 / 3)
df.loc[((df['4_1_2']!=1)&(df['4_1_2']!=2))|
       (df['4_1_7']!=2),'X4m_AG'] = df['X3m_AG']

df['NOTA AGUA'] = np.nan
df.loc[df['4_1_2']!=4,'NOTA AGUA'] = df['X4M_AG'] * .7 + df['X4m_AG'] * .3
df.loc[df['4_1_2']==4,'NOTA AGUA'] = df['X4M_AG']

"""# NOTA ESGOTO"""

df['X1M_ES'] = np.nan
df.loc[(df['4_2_1']==1)&
      (df['4_2_3']==1),'X1M_ES'] = 8
df.loc[(df['4_2_1']==1)&
      (df['4_2_3']==2),'X1M_ES'] = 7
df.loc[(df['4_2_1']==1)&
      (df['4_2_3']==3),'X1M_ES'] = 6
df.loc[(df['4_2_1']==3),'X1M_ES'] = 5
df.loc[(df['4_2_1']==2),'X1M_ES'] = 4
df.loc[(df['4_2_1']==4),'X1M_ES'] = 3
df.loc[(df['4_2_1']==5),'X1M_ES'] = 2
df.loc[(df['4_2_1']==6)|
       (df['4_2_1']==7),'X1M_ES'] = 1
df['X1M_ES'] = (df['X1M_ES'] / 8) * 6

df['X1m_ES'] = np.nan
df.loc[(df['4_2_5']==1)&
      (df['4_2_7']==1),'X1m_ES'] = 8
df.loc[(df['4_2_5']==1)&
      (df['4_2_7']==2),'X1m_ES'] = 7
df.loc[(df['4_2_5']==1)&
      (df['4_2_7']==3),'X1m_ES'] = 6
df.loc[(df['4_2_5']==3),'X1m_ES'] = 5
df.loc[(df['4_2_5']==2),'X1m_ES'] = 4
df.loc[(df['4_2_5']==4),'X1m_ES'] = 3
df.loc[(df['4_2_5']==5),'X1m_ES'] = 2
df.loc[(df['4_2_5']==6)|
       (df['4_2_5']==7),'X1m_ES'] = 1
df['X1m_ES'] = (df['X1m_ES'] / 8) * 6

df['X2M_ES'] = df['X1M_ES']
df.loc[(df['4_2_2']==1)|
       (df['4_2_2']==0),'X2M_ES'] = df['X1M_ES']
df.loc[(df['4_2_2']==2),'X2M_ES'] = df['X1M_ES'] - .3
df.loc[(df['4_2_2']==3),'X2M_ES'] = df['X1M_ES'] - .6

"""**Aqui eu alterei pois eu acho que o valor de 4_2_2 caso não seja na rede oficial ou não oficial, o Kobo deveria preencher automaticamente o valor 0, e não deixar em branco. Por conta disso, já defino a variável X2M == X1M. Essa ideia está de acordo com o Excel que explica como calcular os pesos.**"""

df['X2m_ES'] = df['X1m_ES']
df.loc[(df['4_2_6']==1)|
       (df['4_2_6']==0),'X2m_ES'] = df['X1m_ES']
df.loc[(df['4_2_6']==2),'X2m_ES'] = df['X1m_ES'] - .3
df.loc[(df['4_2_6']==3),'X2m_ES'] = df['X1m_ES'] - .6

"""**Aqui eu alterei pois eu acho que o valor de 4_2_6 caso não seja na rede oficial ou não oficial, o Kobo deveria preencher automaticamente o valor 0, e não deixar em branco. Por conta disso, já defino a variável X2m == X1m. Essa ideia está de acordo com o Excel que explica como calcular os pesos.**"""

df['X2_ES'] = df['X2M_ES']
df.loc[(df['4_2_5']!=8),'X2_ES'] = df['X2M_ES'] * .7 + df['X2m_ES'] * .3

df['Y1_ES'] = np.nan
df.loc[(df['4_2_10']==1),'Y1_ES'] = 1
df.loc[(df['4_2_10']==2)&
      (df['4_2_11']==1),'Y1_ES'] = .7
df.loc[(df['4_2_10']==2)&
      (df['4_2_11']==2),'Y1_ES'] = .54
df.loc[(df['4_2_10']==2)&
      (df['4_2_11']==3),'Y1_ES'] = .38
df.loc[(df['4_2_10']==3)&
      (df['4_2_11']==1),'Y1_ES'] = .62
df.loc[(df['4_2_10']==3)&
      (df['4_2_11']==2),'Y1_ES'] = .46
df.loc[(df['4_2_10']==3)&
      (df['4_2_11']==3),'Y1_ES'] = .3
df.loc[(df['4_2_10']==4)&
      (df['4_2_11']==1),'Y1_ES'] = .54
df.loc[(df['4_2_10']==4)&
      (df['4_2_11']==2),'Y1_ES'] = .38
df.loc[(df['4_2_10']==4)&
      (df['4_2_11']==3),'Y1_ES'] = .22
df.loc[(df['4_2_10']==5)&
      (df['4_2_11']==1),'Y1_ES'] = .46
df.loc[(df['4_2_10']==5)&
      (df['4_2_11']==2),'Y1_ES'] = .3
df.loc[(df['4_2_10']==5)&
      (df['4_2_11']==3),'Y1_ES'] = .14

df['Y2_ES'] = np.nan
df.loc[(df['4_2_9']==1)|
      (df['4_2_9']==6),'Y2_ES'] = 1
df.loc[(df['4_2_9']==2),'Y2_ES'] = .7
df.loc[(df['4_2_9']==3),'Y2_ES'] = .55
df.loc[(df['4_2_9']==4),'Y2_ES'] = .4
df.loc[(df['4_2_9']==5),'Y2_ES'] = .25

df['Y3_ES'] = np.nan
df.loc[(df['Y1_ES'] >= df['Y2_ES']),'Y3_ES'] = df['Y2_ES']
df.loc[(df['Y1_ES'] < df['Y2_ES']),'Y3_ES'] = df['Y1_ES']

df['NOTA ESGOTO'] = df['X2_ES'] * df['Y3_ES']

"""# NOTA DRENAGEM"""

df['X1_DR'] = np.nan
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==2)&
       (df['4_3_3']==1)&
      (df['4_3_5']==1),'X1_DR'] = 40
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==2)&
       (df['4_3_3']==1)&
      (df['4_3_5']==2),'X1_DR'] = 32
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==2)&
       (df['4_3_3']==1)&
      (df['4_3_5']==3),'X1_DR'] = 24
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==2)&
       (df['4_3_3']==1)&
      (df['4_3_5']==4),'X1_DR'] = 16
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==2)&
       (df['4_3_3']==1)&
      (df['4_3_5']==5),'X1_DR'] = 8
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==2)&
       (df['4_3_3']==2)&
      (df['4_3_5']==1),'X1_DR'] = 39
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==2)&
       (df['4_3_3']==2)&
      (df['4_3_5']==2),'X1_DR'] = 31
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==2)&
       (df['4_3_3']==2)&
      (df['4_3_5']==3),'X1_DR'] = 23
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==2)&
       (df['4_3_3']==2)&
      (df['4_3_5']==4),'X1_DR'] = 15
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==2)&
       (df['4_3_3']==2)&
      (df['4_3_5']==5),'X1_DR'] = 7
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==2)&
       (df['4_3_3']==3)&
      (df['4_3_5']==1),'X1_DR'] = 38
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==2)&
       (df['4_3_3']==3)&
      (df['4_3_5']==2),'X1_DR'] = 30
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==2)&
       (df['4_3_3']==3)&
      (df['4_3_5']==3),'X1_DR'] = 22
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==2)&
       (df['4_3_3']==3)&
      (df['4_3_5']==4),'X1_DR'] = 14
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==2)&
       (df['4_3_3']==3)&
      (df['4_3_5']==5),'X1_DR'] = 6

df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==1)&
       (df['4_3_3']==1)&
      (df['4_3_5']==1),'X1_DR'] = 36
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==1)&
       (df['4_3_3']==1)&
      (df['4_3_5']==2),'X1_DR'] = 29
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==1)&
       (df['4_3_3']==1)&
      (df['4_3_5']==3),'X1_DR'] = 21
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==1)&
       (df['4_3_3']==1)&
      (df['4_3_5']==4),'X1_DR'] = 13
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==1)&
       (df['4_3_3']==1)&
      (df['4_3_5']==5),'X1_DR'] = 5
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==1)&
       (df['4_3_3']==2)&
      (df['4_3_5']==1),'X1_DR'] = 35
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==1)&
       (df['4_3_3']==2)&
      (df['4_3_5']==2),'X1_DR'] = 28
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==1)&
       (df['4_3_3']==2)&
      (df['4_3_5']==3),'X1_DR'] = 20
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==1)&
       (df['4_3_3']==2)&
      (df['4_3_5']==4),'X1_DR'] = 12
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==1)&
       (df['4_3_3']==2)&
      (df['4_3_5']==5),'X1_DR'] = 4
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==1)&
       (df['4_3_3']==3)&
      (df['4_3_5']==1),'X1_DR'] = 34
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==1)&
       (df['4_3_3']==3)&
      (df['4_3_5']==2),'X1_DR'] = 27
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==1)&
       (df['4_3_3']==3)&
      (df['4_3_5']==3),'X1_DR'] = 19
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==1)&
       (df['4_3_3']==3)&
      (df['4_3_5']==4),'X1_DR'] = 11
df.loc[(df['4_3_1']==1)&
       (df['4_3_2']==1)&
       (df['4_3_3']==3)&
      (df['4_3_5']==5),'X1_DR'] = 3

df.loc[(df['4_3_1']==2)&
       (df['4_3_2']==1)&
      (df['4_3_5']==1),'X1_DR'] = 33
df.loc[(df['4_3_1']==2)&
       (df['4_3_2']==1)&
      (df['4_3_5']==2),'X1_DR'] = 26
df.loc[(df['4_3_1']==2)&
       (df['4_3_2']==1)&
      (df['4_3_5']==3),'X1_DR'] = 18
df.loc[(df['4_3_1']==2)&
       (df['4_3_2']==1)&
      (df['4_3_5']==4),'X1_DR'] = 10
df.loc[(df['4_3_1']==2)&
       (df['4_3_2']==1)&
      (df['4_3_5']==5),'X1_DR'] = 2

df.loc[(df['4_3_1']==2)&
       (df['4_3_2']==2)&
      (df['4_3_5']==1),'X1_DR'] = 37
df.loc[(df['4_3_1']==2)&
       (df['4_3_2']==2)&
      (df['4_3_5']==2),'X1_DR'] = 25
df.loc[(df['4_3_1']==2)&
       (df['4_3_2']==2)&
      (df['4_3_5']==3),'X1_DR'] = 17
df.loc[(df['4_3_1']==2)&
       (df['4_3_2']==2)&
      (df['4_3_5']==4),'X1_DR'] = 9
df.loc[(df['4_3_1']==2)&
       (df['4_3_2']==2)&
      (df['4_3_5']==5),'X1_DR'] = 1

df['X1_DR'] = (df['X1_DR'] / 40) * 6

df['NOTA DRENAGEM'] = df['X1_DR']
df.loc[(df['4_3_4']!=2)&(df['4_3_4']!=0),
      'NOTA DRENAGEM'] = df['X1_DR'] - .1

"""# NOTA LIXO"""

df['D1_LI'] = 0
df.loc[(df['4_4_1']!=1)&
      (df['4_4_3']==1),'D1_LI'] = .95
df.loc[(df['4_4_1']!=1)&
      (df['4_4_3']==2),'D1_LI'] = .9
df.loc[(df['4_4_1']!=1)&
      (df['4_4_3']==3),'D1_LI'] = .75
df.loc[(df['4_4_1']!=1)&
      (df['4_4_3']==4),'D1_LI'] = .7
df.loc[(df['4_4_1']!=1)&
      (df['4_4_3']==5),'D1_LI'] = .5

df['D2_LI'] = 0
df.loc[df['4_4_4']==1,'D2_LI'] = .95
df.loc[df['4_4_4']==2,'D2_LI'] = .9
df.loc[df['4_4_4']==3,'D2_LI'] = .75
df.loc[df['4_4_4']==4,'D2_LI'] = .7
df.loc[df['4_4_4']==5,'D2_LI'] = .5
df.loc[df['4_4_4']==6,'D2_LI'] = df['D1_LI']

df['D1_D2_LI'] = df['D1_LI'] * .5 + df['D2_LI'] * .5
df['D_LI'] = df[['D1_LI','D1_D2_LI']].max(axis=1)

df['P_LI'] = np.nan
df.loc[df['4_4_1']==1,'P_LI'] = 1
df.loc[df['4_4_1']==2,'P_LI'] = .7
df.loc[df['4_4_1']==3,'P_LI'] = .3
df.loc[df['4_4_1']==4,'P_LI'] = 0

df['X1_LI'] = 6

df['X2_LI'] = df['X1_LI'] * df['D_LI']

df['X_LI'] = df['X1_LI'] * df['P_LI'] + df['X2_LI'] * (1 - df['P_LI'])

df['A_LI'] = np.nan
df.loc[((df['4_4_6']==2)|
      (df['4_4_6']==3))&
      (df['4_4_7']==1)&
      (df['4_4_8']==1)&
      (df['4_4_9']==1),'A_LI'] = 1
df.loc[(df['4_4_6']==1)&
      (df['4_4_7']==1)&
      (df['4_4_8']==1)&
      (df['4_4_9']==1),'A_LI'] = .95
df.loc[(df['4_4_7']==2)&
      (df['4_4_8']==1)&
      (df['4_4_9']==1),'A_LI'] = .9
df.loc[(df['4_4_7']==3)&
      (df['4_4_8']==1)&
      (df['4_4_9']==1),'A_LI'] = .8
df.loc[(df['4_4_7']==4)&
      (df['4_4_8']==1)&
      (df['4_4_9']==1),'A_LI'] = .8
df.loc[(df['4_4_7']==5)&
      (df['4_4_8']==1)&
      (df['4_4_9']==1),'A_LI'] = .7
df.loc[(df['4_4_8']==2)&
      (df['4_4_9']==1),'A_LI'] = .65
df.loc[(df['4_4_8']==3)&
      (df['4_4_9']==1),'A_LI'] = .5
df.loc[(df['4_4_8']==4)&
      (df['4_4_9']==1),'A_LI'] = .5
df.loc[(df['4_4_8']==5)&
      (df['4_4_9']==1),'A_LI'] = .35
df.loc[(df['4_4_9']==2),'A_LI'] = .2

df['E_LI'] = np.nan
df.loc[df['4_4_11']==1,'E_LI'] = 1
df.loc[df['4_4_11']==2,'E_LI'] = .95
df.loc[df['4_4_11']==3,'E_LI'] = .9

df['NOTA LIXO'] = df['X_LI'] * df['A_LI'] * df['E_LI']

"""# NOTA ENERGIA ELÉTRICA"""

df['X_EE'] = 6

df['L_EE'] = np.nan
df.loc[df['4_5_1']==1,'L_EE'] = 1
df.loc[df['4_5_1']==2,'L_EE'] = .9
df.loc[df['4_5_1']==3,'L_EE'] = .7
df.loc[df['4_5_1']==4,'L_EE'] = .5

df['I_EE'] = np.nan
df.loc[df['4_5_2']==1,'I_EE'] = 1
df.loc[df['4_5_2']==2,'I_EE'] = .8
df.loc[df['4_5_2']==3,'I_EE'] = .5
df.loc[df['4_5_2']==4,'I_EE'] = .3

df['NOTA ENERGIA'] = df['X_EE'] * df['L_EE'] * df['I_EE']

"""# NOTA ILUMINAÇÃO"""

df['D1_IL'] = np.nan
df.loc[df['4_6_2']==1,'D1_IL'] = 1
df.loc[df['4_6_2']==2,'D1_IL'] = .9
df.loc[df['4_6_2']==3,'D1_IL'] = .6

df['D2_IL'] = np.nan
df.loc[df['4_6_3']==1,'D2_IL'] = 1
df.loc[df['4_6_3']==2,'D2_IL'] = .9
df.loc[df['4_6_3']==3,'D2_IL'] = .6

df['D_IL'] = np.nan
df.loc[(df['4_6_2']!=4)&
      (df['4_6_3']!=4),'D_IL'] = (df['D1_IL'] * .5) + (df['D2_IL'] * .5)
df.loc[(df['4_6_2']==4)&
      (df['4_6_3']<4),'D_IL'] = df['D2_IL']
df.loc[(df['4_6_2']<4)&
      (df['4_6_3']==4),'D_IL'] = df['D1_IL']
df.loc[(df['4_6_2']==4)&
      (df['4_6_3']==4),'D_IL'] = np.nan

df['R_IL'] = np.nan
df.loc[df['4_6_4']==1,'R_IL'] = 1
df.loc[df['4_6_4']==2,'R_IL'] = .8
df.loc[df['4_6_4']==3,'R_IL'] = .5

df['X_IL'] = 6 * df['D_IL'] * df['R_IL']
df.loc[df['D_IL'].isnull(),'X_IL'] = 0

df['P_IL'] = np.nan
df.loc[df['4_6_1']==1,'P_IL'] = 1
df.loc[df['4_6_1']==2,'P_IL'] = .7
df.loc[df['4_6_1']==3,'P_IL'] = .3
df.loc[df['4_6_1']==4,'P_IL'] = 0

df['NOTA ILUMINAÇÃO'] = ((df['X_IL'] * df['P_IL']) + (1 * (1 - df['P_IL']) * 2)) / (df['P_IL'] * 1 + (1 - df['P_IL']) * 2)

"""***"""

pd.set_option('display.max_columns', None)


print(list(df[df.columns[pd.Series(df.columns).str.startswith('NOTA')]]))

notas = df[['v003','NOTA PLACAS E CORREIOS', 'NOTA INFRA PARA MOBILIDADE', 'NOTA TRANSPORTE', 'NOTA MORADIA',
            'NOTA AGUA', 'NOTA ESGOTO', 'NOTA DRENAGEM', 'NOTA LIXO', 'NOTA ENERGIA', 'NOTA ILUMINAÇÃO']]

notas['NOTA GERAL'] = notas[['NOTA AGUA', 'NOTA DRENAGEM', 'NOTA ENERGIA', 'NOTA ESGOTO', 'NOTA ILUMINAÇÃO',
                         'NOTA INFRA PARA MOBILIDADE', 'NOTA LIXO', 'NOTA MORADIA', 'NOTA PLACAS E CORREIOS',
                         'NOTA TRANSPORTE']].mean(axis=1)

"""### OUTPUTS"""

data_atual = datetime.datetime.now().strftime('%Y%m%d')

df.to_csv(f'{data_atual}_notas_kobo_completa.csv',index=False)
notas.to_csv(f'{data_atual}_notas_kobo.csv',index=False)
df.to_excel(f'{data_atual}_notas_kobo_completa.xlsx',index=False)
notas.to_excel(f'{data_atual}_notas_kobo.xlsx',index=False)
