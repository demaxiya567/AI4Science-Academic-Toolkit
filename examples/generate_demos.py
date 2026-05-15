#!/usr/bin/env python3
"""Generate all demo figures for the toolkit README.
All data is synthetic/public — no real research data.
"""
import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), 'demo_output')
os.makedirs(OUT, exist_ok=True)

# Apply toolkit style
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from module_02_visualization.scripts.style_presets import get_base_style
import matplotlib as mpl
mpl.rcParams.update(get_base_style())
COLORS = ['#E69F00','#56B4E9','#009E73','#F0E442','#0072B2','#D55E00','#CC79A7']
np.random.seed(42)

def save(fig, name):
    fig.savefig(os.path.join(OUT, f'{name}.pdf'))
    fig.savefig(os.path.join(OUT, f'{name}.png'), dpi=150)
    plt.close(fig)
    print(f'  [OK] {name}')

# 1. BAR CHART
fig, ax = plt.subplots(figsize=(3.5, 2.8))
cats = ['Fresh', '200 h', '500 h', '1000 h']
vals, errs = [94.2, 88.5, 76.3, 62.1], [1.8, 2.1, 3.5, 4.2]
ax.bar(cats, vals, yerr=errs, color=COLORS[:4], capsize=3, edgecolor='white', lw=0.5)
ax.set_ylabel('Conversion (%)'); ax.set_ylim(0, 105)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
fig.tight_layout(); save(fig, 'demo_bar')

# 2. MULTI-PANEL
fig, axes = plt.subplots(2, 2, figsize=(7, 5.5))
x = np.linspace(0, 10, 50)
for i, lbl in enumerate(['200 C','250 C','300 C','350 C']):
    y = 100/(1+np.exp(-0.8*(x-(2+i*1.8)))) + np.random.normal(0,1.5,50)
    axes[0,0].plot(x, y, color=COLORS[i], label=lbl, lw=1)
axes[0,0].set_ylabel('Conversion (%)'); axes[0,0].legend(fontsize=6, frameon=False)
axes[0,0].spines['top'].set_visible(False); axes[0,0].spines['right'].set_visible(False)
axes[0,0].text(-0.15,1.05,'a',transform=axes[0,0].transAxes,fontweight='bold',fontsize=11)

angles = np.arange(10,70,0.05)
pattern = np.zeros_like(angles)
for pos,h in [(18,0.8),(22,0.3),(27.5,1.0),(32,0.4),(36,0.5),(45,0.3),(52,0.2),(58,0.15)]:
    pattern += h * np.exp(-0.5*((angles-pos)/0.3)**2)
pattern += np.random.normal(0,0.02,len(angles))
axes[0,1].plot(angles, pattern, 'k-', lw=0.6)
axes[0,1].set_xlabel('2Theta (degree)'); axes[0,1].set_ylabel('Intensity (a.u.)')
axes[0,1].spines['top'].set_visible(False); axes[0,1].spines['right'].set_visible(False)
axes[0,1].text(-0.15,1.05,'b',transform=axes[0,1].transAxes,fontweight='bold',fontsize=11)

corr = np.array([[1.00,0.82,-0.45,0.12],[0.82,1.00,-0.63,0.08],[-0.45,-0.63,1.00,-0.31],[0.12,0.08,-0.31,1.00]])
im = axes[1,0].imshow(corr, cmap='RdBu_r', vmin=-1, vmax=1, aspect='equal')
for lbls in [['Temp','Conv','Select','Yield']]*2:
    axes[1,0].set_xticks(range(4)); axes[1,0].set_xticklabels(lbls,fontsize=7)
    axes[1,0].set_yticks(range(4)); axes[1,0].set_yticklabels(lbls,fontsize=7)
for i in range(4):
    for j in range(4):
        axes[1,0].text(j,i,f'{corr[i,j]:.2f}',ha='center',va='center',fontsize=7)
axes[1,0].text(-0.15,1.05,'c',transform=axes[1,0].transAxes,fontweight='bold',fontsize=11)

xv = np.linspace(0,1,50); yv = 4*xv*(1-xv)*100 + np.random.normal(0,3,50)
axes[1,1].scatter(xv, yv, c=COLORS[0], s=12, alpha=0.7, edgecolors='none')
axes[1,1].plot(np.linspace(0,1,100), np.poly1d(np.polyfit(xv,yv,2))(np.linspace(0,1,100)),'--',color='#999999',lw=1)
axes[1,1].set_xlabel('Descriptor value'); axes[1,1].set_ylabel('Activity (a.u.)')
axes[1,1].spines['top'].set_visible(False); axes[1,1].spines['right'].set_visible(False)
axes[1,1].text(-0.15,1.05,'d',transform=axes[1,1].transAxes,fontweight='bold',fontsize=11)
fig.tight_layout(); save(fig, 'demo_multipanel')

# 3. XPS
from scipy.ndimage import gaussian_filter1d
fig, ax = plt.subplots(figsize=(4, 2.8))
be = np.linspace(540,525,500)
s = gaussian_filter1d(np.random.rand(500)*0.5,8) + 3*np.exp(-0.5*((be-532)/0.8)**2) + 1.5*np.exp(-0.5*((be-534)/0.9)**2) + 0.8*np.exp(-0.5*((be-536)/1.0)**2)
ax.plot(be, s, 'k-', lw=0.8)
ax.set_xlabel('Binding Energy (eV)'); ax.set_ylabel('Intensity (a.u.)'); ax.invert_xaxis()
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.annotate('O 1s', xy=(532,3.0), fontsize=7, fontstyle='italic')
fig.tight_layout(); save(fig, 'demo_xps')

# 4. MULTI-LINE
fig, ax = plt.subplots(figsize=(3.5,2.6))
x = np.linspace(0,720,100)
for i,(m,base,decay) in enumerate(zip(['Cat-A','Cat-B','Cat-C','Cat-D (Ours)'],[94,88,82,97],[0.08,0.15,0.25,0.04])):
    ax.plot(x, base*np.exp(-decay*x/720)+np.random.normal(0,0.5,100), color=COLORS[i], lw=1.5 if i==3 else 1.0, ls='-' if i==3 else '--', label=m)
ax.set_xlabel('Time on Stream (h)'); ax.set_ylabel('Conversion (%)')
ax.legend(fontsize=6,frameon=False); ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
fig.tight_layout(); save(fig, 'demo_lines')

# 5. TEM-lIKE
fig, ax = plt.subplots(figsize=(3,3))
nx, ny = 200, 200
Y, X = np.mgrid[:nx, :ny]
d2 = (X-nx//2)**2 + (Y-ny//2)**2
mask = d2 < 60**2
img = np.random.rand(nx, ny) * 0.3
img[mask] = 0.8 + 0.2 * np.random.rand(*img[mask].shape)
img[mask] += 0.15 * np.sin(20 * X[mask]) * np.exp(-d2[mask]/(2*40**2))
ax.imshow(img, cmap='gray', extent=[0,50,0,50])
ax.set_xlabel('nm'); ax.set_ylabel('nm')
fig.tight_layout(); save(fig, 'demo_tem')

# SUMMARY
with open(os.path.join(OUT,'SUMMARY.txt'),'w',encoding='utf-8') as f:
    f.write('''Demo Figures - AI4Science Academic Toolkit
=========================================
bar chart, multi-panel (curves/XRD/heatmap/volcano),
XPS spectrum, multi-line comparison, simulated TEM
All data is synthetic/generic. No real research data.
''')
print(f'  [OK] SUMMARY.txt')
print(f'\nDone! All files in {OUT}/')
