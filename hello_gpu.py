#
# 📖 [PyCUDAを使ってみよう](https://scrapbox.io/PythonOsaka/PyCUDA%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%BF%E3%82%88%E3%81%86)
#
#   ```
#   %windir%\system32\cmd.exe "/K" %USERPROFILE%\Anaconda3\Scripts\activate.bat %USERPROFILE%\Anaconda3
#   python hello_gpu.py
#   ```
#
import pycuda.autoinit
import pycuda.driver as drv
import numpy

from pycuda.compiler import SourceModule
mod = SourceModule("""
__global__ void multiply_them(float *dest, float *a, float *b)
{
  const int i = threadIdx.x;
  dest[i] = a[i] * b[i];
}
""")

multiply_them = mod.get_function("multiply_them")

a = numpy.random.randn(400).astype(numpy.float32)
b = numpy.random.randn(400).astype(numpy.float32)

dest = numpy.zeros_like(a)
multiply_them(
        drv.Out(dest), drv.In(a), drv.In(b),
        block=(400,1,1), grid=(1,1))

print(dest-a*b)
