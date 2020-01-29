import sys
from cx_Freeze import setup, Executable


base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Programa de pagos embajadores",
      version="1.0",
      description="Generador de pagos de actividades.",
      executables=[Executable("PlanillasPagos.py", base=base)])