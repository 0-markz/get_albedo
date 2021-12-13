import numpy as np
import matplotlib.pyplot as plt
import imageio
from cycler import cycler

def readIntensity(photoName, plotName, lamp, surface, x1, x2, y1, y2, a1, a2, ylim = True):
    
    photo = imageio.imread(photoName)
    
    background = photo[x1:x2, y1:y2, a1:a2].swapaxes(0, 1)
    
    cut = photo[x1:x2, y1:y2, a1:a2].swapaxes(0, 1)
    
    rgb = np.mean(cut, axis=(0))
    
    #print(rgb.shape)
    
    luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]
    
    #luma - brightness

    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'chartreuse', 'deepskyblue'])))

    fig = plt.figure(figsize=(10, 5), dpi=400)

    plt.title('Интенсивность отражённого излучения\n' + '{} / {}'.format(lamp, surface))
    
    plt.xlabel('Относительный номер элемента изображения')
    plt.ylabel('Яркость')
    
    #plt.plot(rgb, label = ['red', 'green', 'blue'] )[i for i in range(len(rgb[0, :]))], 

    plt.plot(rgb[:, 0], label = 'R' )
    plt.plot(rgb[:, 1], label = 'G' )
    plt.plot(rgb[:, 2], label = 'B')
    
    plt.plot(1*luma, 'w', label = 'Itensity')
    
    loc, labl = plt.yticks()
    
    if (ylim):
    
        plt.ylim(0,np.max(rgb))
    
    
    #plt.yticks(np.arange(0, 81, 20))
    
    plt.legend(loc = 'best')
    
    ax = fig.add_subplot(111)
    ax.patch.set_facecolor('dimgray')
    ax.patch.set_alpha(1.0)
    
    plt.imshow(background, origin='lower')
    
    
    plt.savefig(plotName, pad_inches = 0.001)

    return luma