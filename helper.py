# display imports
import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(scores, mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    # Format with two decimal places using f-string
    plt.text(len(scores)-1, scores[-1], f"{scores[-1]:.2f}")
    plt.text(len(mean_scores)-1, mean_scores[-1], f"{mean_scores[-1]:.2f}")