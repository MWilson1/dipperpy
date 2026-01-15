import matplotlib.pyplot as plt
import dipperpy.lightspinner as dp_ls 

AtomSpect = dp_ls.atomicspectrum()
wvls, intensities = AtomSpect.spectrum( ['CaII_medium', 'MgII'] ) 


plt.figure()
plt.plot( wvls, intensities[:,-1] )
plt.ylabel(r"I [ J s$^{-1}$ m$^{-2}$ sr$^{-1}\ \AA^{-1}$ ]", fontfamily="Times New Roman")
plt.xlabel(r"$\lambda$ [nm]", fontfamily="Times New Roman")
plt.show()
#plt.close()


