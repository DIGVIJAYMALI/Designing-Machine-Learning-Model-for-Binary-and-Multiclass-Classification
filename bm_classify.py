import numpy as np


def binary_train(X, y, loss="perceptron", w0=None, b0=None, step_size=0.5, max_iterations=1000):
    """
    Inputs:
    - X: training features, a N-by-D numpy array, where N is the 
    number of training points and D is the dimensionality of features
    - y: binary training labels, a N dimensional numpy array where 
    N is the number of training points, indicating the labels of 
    training data
    - loss: loss type, either perceptron or logistic
    - step_size: step size (learning rate)
	- max_iterations: number of iterations to perform gradient descent

    Returns:
    - w: D-dimensional vector, a numpy array which is the weight 
    vector of logistic or perceptron regression
    - b: scalar, which is the bias of logistic or perceptron regression
    """
    N, D = X.shape
    assert len(np.unique(y)) == 2


    w = np.zeros(D)
    if w0 is not None:
        w = w0
    
    b = 0
    if b0 is not None:
        b = b0

    if loss == "perceptron":
        ############################################
        # TODO 1 : Edit this if part               #
        #          Compute w and b here            #
        #for i in len(y):
        #    if(y[i]==0):
        #        y[i]=-1
   
        w = np.zeros(D)
        b = 0
        for j in range(len(y)):
            if(y[j]>0):
              y[j]=1
            else:
              y[j]=-1
        ############################################
        for i in range(max_iterations):
            i=np.multiply(y,np.dot(X,w)+b)<=0
            Xi=X[i]
            Yi=y[i]
            w+=step_size*(1/N)*np.dot(Xi.transpose(),Yi)
            b+=step_size*(1/N)*np.sum(Yi)

    elif loss == "logistic":
        ############################################
        # TODO 2 : Edit this if part               #
        #          Compute w and b here            #
        w = np.zeros(D)
        b = 0
      
        ############################################
        
        ############################################
        for i in range(max_iterations):
            yn=sigmoid(np.dot(X,w)+b)
            w-=step_size*(1/N)*np.dot(X.transpose(),yn-y)
            b-=step_size*(1/N)*np.sum(yn-y)


        ############################################
        

    else:
        raise "Loss Function is undefined."

    #assert w.shape == (D,)
    return w, b

def sigmoid(z):
    
    """
    Inputs:
    - z: a numpy array or a float number
    
    Returns:
    - value: a numpy array or a float number after computing sigmoid function value = 1/(1+exp(-z)).
    """
    
    return 1/(1+np.exp(-z))


    
def binary_predict(X, w, b, loss="perceptron"):
    """
    Inputs:
    - X: testing features, a N-by-D numpy array, where N is the 
    number of training points and D is the dimensionality of features
    - w: D-dimensional vector, a numpy array which is the weight 
    vector of your learned model
    - b: scalar, which is the bias of your model
    - loss: loss type, either perceptron or logistic
    
    Returns:
    - preds: N dimensional vector of binary predictions: {0, 1}
    """
    N, D = X.shape
    
    if loss == "perceptron":
        ############################################
        # TODO 4 : Edit this if part               #
        #          Compute preds                   #
        preds = np.zeros(N)
        preds=np.dot(X,w)+b
        preds[preds<=0]=0
        preds[preds>0]=1
        ############################################
        

    elif loss == "logistic":
        ############################################
        # TODO 5 : Edit this if part               #
        #          Compute preds                   #
        preds = np.zeros(N)
        preds=sigmoid(np.dot(X,w)+b)
        preds[preds>0.5]=1
        preds[preds<=0.5]=0
        
        ############################################
        

    else:
        raise "Loss Function is undefined."
    

    assert preds.shape == (N,) 
    return preds

def softmax(N):
    #N= NUMERATOR
    #D=DENOMINATOR
    N = np.exp(N-np.amax(N))
    #N HAS EXPONENT OF ALL ELEMENTS IN N
    D = np.sum(N, axis=1)
    #D IS SUM OF EXPONENTS OF ELEMENTS IN EACH ROW OF N
    return (N.T / D).T



def multiclass_train(X, y, C,
                     w0=None, 
                     b0=None,
                     gd_type="sgd",
                     step_size=0.5, 
                     max_iterations=1000):
    """
    Inputs:
    - X: training features, a N-by-D numpy array, where N is the 
    number of training points and D is the dimensionality of features
    - y: multiclass training labels, a N dimensional numpy array where
    N is the number of training points, indicating the labels of 
    training data
    - C: number of classes in the data
    - gd_type: gradient descent type, either GD or SGD
    - step_size: step size (learning rate)
    - max_iterations: number of iterations to perform gradient descent

    Returns:
    - w: C-by-D weight matrix of multinomial logistic regression, where 
    C is the number of classes and D is the dimensionality of features.
    - b: bias vector of length C, where C is the number of classes
    """

    N, D = X.shape

    w = np.zeros((C, D))
    if w0 is not None:
        w = w0
    
    b = np.zeros(C)
    if b0 is not None:
        b = b0
     
              
        
    np.random.seed(42)

    #CONVERT Y[Nx1] TO y[NxC] NEED TO DO NEXT STEP
    y1=y
    y = np.eye(C)[y]
    
    if gd_type == "sgd":
        ############################################
        # TODO 6 : Edit this if part               #
        #          Compute w and b                 #
        w = np.zeros((C, D))
        b = np.zeros(C)
        ############################################
      
        ############################################
        for i in range(max_iterations):
            k=np.random.choice(N)
            x=np.dot(w,X[k])+b
            soft=np.exp(x-x.max())
            soft=soft/np.sum(soft)
            yn=soft
            yn[y1[k]]=yn[y1[k]]-1
            w-=(step_size*np.reshape(yn,(C,1))*X[k])
            b-=(step_size*soft)

  

    elif gd_type == "gd":
        ############################################
        # TODO 7 : Edit this if part               #
        #          Compute w and b                 #
        w = np.zeros((C, D))
        b = np.zeros(C)
        ############################################
        
        for i in range(max_iterations):
            yn = softmax((np.dot(X,w.T)) + b.T)  
            w -= step_size*(1/N)*(yn-y).T.dot(X)
            b -= step_size*(1/N)*np.sum(yn-y, axis=0)
           
    else:
        raise "Type of Gradient Descent is undefined."
    

    assert w.shape == (C, D)
    assert b.shape == (C,)

    return w, b


def multiclass_predict(X, w, b):
    """
    Inputs:
    - X: testing features, a N-by-D numpy array, where N is the 
    number of training points and D is the dimensionality of features
    - w: weights of the trained multinomial classifier, C-by-D 
    - b: bias terms of the trained multinomial classifier, length of C
    
    Returns:
    - preds: N dimensional vector of multiclass predictions.
    Outputted predictions should be from {0, C - 1}, where
    C is the number of classes
    """
 
    
    N, D = X.shape
    ############################################
    # TODO 8 : Edit this part to               #
    #          Compute preds                   #
    preds = np.zeros(N)
    ############################################
    
    
    preds = softmax((np.dot(X,w.T)) + b)
    preds = np.argmax(preds, axis=1)
    assert preds.shape == (N,)
    return preds




        