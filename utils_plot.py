#!/usr/bin/env python
# coding: utf-8

# In[4]:


def plot_both(history):
    import matplotlib.pyplot as plt
    history_dict = history.history
    acc_values = history_dict["acc"]
    val_acc_values = history_dict["val_acc"]
    loss_values = history_dict["loss"]
    val_loss_values = history_dict["val_loss"]
    
    epochs = range(1, len(loss_values)+1)
    
    fig = plt.figure()
    
    ax1 = fig.add_subplot(1,2,1)
    ax1.plot(epochs, acc_values, label="Training acc")
    ax1.plot(epochs, val_acc_values, label="Validation acc")
    ax1.set_title("Training and validation accuracy")
    ax1.set_xlabel("Epochs")
    ax1.set_ylabel("Acc")
    ax1.legend()
    
    ax2 = fig.add_subplot(1,2,2)
    ax2.plot(epochs, loss_values, label="Training loss")
    ax2.plot(epochs, val_loss_values, label="Validation loss")
    ax2.set_title("Training and validation accuracy")
    ax2.set_xlabel("Epochs")
    ax2.set_ylabel("Loss")
    ax2.legend()
    
    plt.show


# In[5]:


def plot_accuracy(history):
    import matplotlib.pyplot as plt
    history_dict = history.history
    acc_values = history_dict["acc"]
    val_acc_values = history_dict["val_acc"]
    
    epochs = range(1, len(acc_values)+1)
    
    plt.plot(epochs, acc_values, label="Training acc")
    plt.plot(epochs, val_acc_values, label="Validation acc")
    plt.title("Training and validation accuracy")
    plt.xlabel("Epochs")
    plt.ylabel("Acc")
    plt.legend()
    plt.show


# In[6]:


def plot_loss(history):
    import matplotlib.pyplot as plt
    history_dict = history.history
    loss_values = history_dict["loss"]
    val_loss_values = history_dict["val_loss"]
    
    epochs = range(1, len(loss_values)+1)
    
    plt.clf()   #clear figure
    plt.plot(epochs, loss_values, label="Training loss")
    plt.plot(epochs, val_loss_values, label="Validation loss")
    plt.title("Training and validation loss")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.legend()
    plt.show


# In[ ]:




