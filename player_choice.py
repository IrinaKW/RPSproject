#%%

import cv2
from keras.models import load_model
import numpy as np
import pandas as pd
def player_choice():
    pred=[]
    model = load_model('RPS_model.h5', compile=False)

    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 
                'Your Turn! Freeze!', 
                (50, 50), 
                font, 1, 
                (0, 255, 0), 
                2, 
                cv2.LINE_4)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = np.round(model.predict(data),2)
        cv2.imshow('frame', frame)
        pred.append(prediction)
        if cv2.waitKey(5000):
            break
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    pred=pd.DataFrame(np.concatenate(pred), columns=['NONE', 'ROCK', 'PAPER', 'SCISSORS'])
    df2 = pred[pred.columns[pred.mean(axis=0) == np.max(pred.mean(axis=0))]]

    [item]=sorted(df2)

    return(item)


# %%
