"""Volume III palette. Numerical inputs and geometry are preserved."""
import plot_style as common
from plot_style import *
BLUE = "#7188A3"
CYAN = BLUE
ICE = "#E5EAF0"
GREEN = "#829C8B"
GRASS = GREEN
SAGE = "#E8EEE9"
YELLOW = "#B4A16F"
PEACH = "#F1ECDD"
ORANGE = YELLOW
CORAL = RED = "#A7787D"
PURPLE = "#9588A5"
BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL = (
    "#E5EAF0", "#E8EEE9", "#F1ECDD", "#F0E5E6", "#ECE8F0")
PALETTE = [BLUE, GREEN, YELLOW, RED, PURPLE]
def configure():
    common.configure()
    mpl.rcParams.update({"font.size":8, "axes.labelsize":8, "axes.titlesize":8.5,
                         "xtick.labelsize":7.5, "ytick.labelsize":7.5, "legend.fontsize":7.5})
def prepare_figure(fig):
    common.prepare_figure(fig)
    for text in fig.findobj(Text):
        text.set_fontsize(7.5 if getattr(text,'academic_role',None)=='note' else min(text.get_fontsize(),8.5))
def style_record():
    result = common.style_record()
    result.update({"palette_name":"Volume III muted Lancet derivative (author revision)",
                   "palette":PALETTE, "fills":[BLUE_FILL,GREEN_FILL,YELLOW_FILL,RED_FILL,PURPLE_FILL],
                   "font_size_pt":{"body":8,"note":7.5,"max":8.5},
                   "palette_source":"figures/03-models/00-shared/matplotlib/volume3_style.py"})
    return result
