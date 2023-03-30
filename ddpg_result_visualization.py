import matplotlib.pyplot as plt
import numpy as np

def plot_scores(scores:list):
    """Plots a score list.
        
        Params
        ======
        scores (array): a score list
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(np.arange(1, len(scores)+1), scores)
    plt.ylabel('Score')
    plt.xlabel('Episode #')
    plt.show()


def format_episode_score(i_episode, episode_avg_score, moving_avg_score):
    """Returns a formatted episode result.
        
        Params
        ======
        i_episode (int): episode index
        episode_avg_score (float): episode average score
        moving_avg_score (float): moving average score
    """
    return f"Episode: {i_episode}\tEpisode average score: {episode_avg_score:.2f}\tMoving average score: {moving_avg_score:.2f}"