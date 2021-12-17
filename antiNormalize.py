def antiNormalize(y_test_t):
    
    y_test_t=pd.DataFrame(y_test_t)
    y_test_t.columns=['closed']
    
    layer=[1 for index in range(len(predicted_stock_pricepd))]
    y_test_t['layer']= layer
    #y_test_t
    y_test_t=scaler.inverse_transform(y_test_t)
    #y_test_t
    ytest=y_test_t
    ytest=pd.DataFrame(ytest)
    ytest.columns=['close','scores']
    ytest=ytest.drop(['scores'],axis=1)
    ytest=np.array(ytest)
    return ytest
def antiNormalizePredict(predicted_stock_price):
    predicted_stock_pricepd=pd.DataFrame(predicted_stock_price)
    predicted_stock_pricepd.columns=['closed']

    layer=[1 for index in range(len(predicted_stock_pricepd))]
    predicted_stock_pricepd['layer']= layer
    #predicted_stock_pricepd
    predicted_stock_pricepd=np.array(predicted_stock_pricepd)
    predicted_stock_pricepd=scaler.inverse_transform(predicted_stock_pricepd)
    predicted_stock_pricepd111=pd.DataFrame(predicted_stock_pricepd)
    predict=predicted_stock_pricepd111
    predict.columns=['close','scores']
    predict=predict.drop(['scores'],axis=1)
    predict=np.array(predict)
    return predict
