"""Holiday-2026 shipment test.
Nike-specific: Feng Tay USD revenue (factory shipments) Jul-Sep 2026 -> lands in US roughly Aug-Oct.
Industry: US footwear imports (HS 6402-6405 Comtrade, World) for Aug-Oct, where Aug 2026 is estimated from
Census FT-900 Exhibit 15 (SITC 85 footwear, NSA, Aug 2026 release) and Sep-Oct are not yet published.
Also compares the gap to its own history (3-month windows, 2019-2025)."""
import os
import pandas as pd

base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
m = pd.read_csv(os.path.join(base, 'nike_vs_industry_monthly.csv'), index_col=0)

# Census FT-900 August 2026, Exhibit 15 (NSA, $m): footwear imports Aug 2026 2483, Jul 2026 2295, YTD Aug 2026 17760, YTD Aug 2025 18115
sitc = dict(aug26=2483.0, jul26=2295.0, ytd26=17760.0, ytd25=18115.0)
w = m['us_fw_world_usd_m']
scale = sitc['ytd25'] / w.loc['2025-01':'2025-08'].sum()          # SITC85 vs HS6402-6405 level ratio
aug25_est = sitc['ytd25'] - w.loc['2025-01':'2025-07'].sum() * scale
aug_yoy = (sitc['aug26'] / aug25_est - 1) * 100
jul_yoy = (sitc['jul26'] / (w.loc['2025-07'] * scale) - 1) * 100
ytd_yoy = (sitc['ytd26'] / sitc['ytd25'] - 1) * 100
print(f'US footwear imports: Jul 2026 {jul_yoy:.1f}% (SITC-scaled), Aug 2026 {aug_yoy:.1f}% (estimated), Jan-Aug {ytd_yoy:.1f}% (official YTD)')
ind_julaug = (sitc['jul26'] + sitc['aug26']) / (w.loc['2025-07'] * scale + aug25_est) * 100 - 100
print(f'Industry Jul-Aug 2026 combined: {ind_julaug:.1f}%')

ft = m['fengtay_usd_m']
ft_q = (ft.loc['2026-07':'2026-09'].sum() / ft.loc['2025-07':'2025-09'].sum() - 1) * 100
ft_q_prev = (ft.loc['2026-04':'2026-06'].sum() / ft.loc['2025-04':'2025-06'].sum() - 1) * 100
print(f'Feng Tay USD Jul-Sep 2026 {ft_q:.1f}% vs Apr-Jun 2026 {ft_q_prev:.1f}%')
for c in ['laiyih_usd_m', 'fulgent_usd_m', 'pouchen_usd_m']:
    s = m[c]
    print(f'{c} Jul-Sep 2026 {(s.loc["2026-07":"2026-09"].sum() / s.loc["2025-07":"2025-09"].sum() - 1) * 100:.1f}%')
gap_now = ft_q - ind_julaug
print(f'Gap (Feng Tay Jul-Sep minus industry Jul-Aug): {gap_now:.1f} pts')

# history: 3-month FT YoY minus US world imports YoY for same 3 months shifted +1
rows = []
idx = list(m.index)
for i in range(12, len(idx) - 3):
    a, b = idx[i], idx[i + 2]
    a1, b1 = idx[i + 1], idx[i + 3]
    pa, pb, pa1, pb1 = idx[i - 12], idx[i - 10], idx[i - 11], idx[i - 9]
    f = ft.loc[a:b].sum() / ft.loc[pa:pb].sum() - 1
    u = w.loc[a1:b1].sum() / w.loc[pa1:pb1].sum() - 1
    if pd.notna(f) and pd.notna(u) and w.loc[a1:b1].count() == 3:
        rows.append(dict(start=a, ft_3m_yoy=f * 100, us_world_3m_yoy_lead1=u * 100, gap=(f - u) * 100))
h = pd.DataFrame(rows).set_index('start')
h.round(2).to_csv(os.path.join(base, 'test_holiday_gap_history.csv'))
hh = h.loc['2019-01':'2025-12', 'gap']
print(f'History 2019-2025 3m gap: mean {hh.mean():.1f}, sd {hh.std():.1f}, n {len(hh)}; share below {gap_now:.1f}: {(hh < gap_now).mean() * 100:.0f}%')
hh2 = h.loc['2023-01':'2025-12', 'gap']
print(f'History 2023-2025 3m gap: mean {hh2.mean():.1f}, sd {hh2.std():.1f}; share below now: {(hh2 < gap_now).mean() * 100:.0f}%')
print(h.loc['2025-06':].round(1).to_string())
