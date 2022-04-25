import matplotlib.pyplot as plt

def bar_chart(numbers, labels, pos):
    fig = plt.figure(figsize=(5,8))
    plt.bar(pos, numbers, color='red')
    #add watermark
    fig.text(1, 0.15, 'mice vs python',
        fontsize = 45,
        color='blue',
        ha='right',
        va='bottom',
        alpha=0.4,
        rotation=25)
    plt.xticks(ticks=pos, labels = labels)
    plt.show()


numbers=[2,1,4,6]
labels = ['Electric','solar','diesel','unleaded']
pos =list(range(4))
bar_chart(numbers,labels, pos)       