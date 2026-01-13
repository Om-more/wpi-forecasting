import pickle
from bajra_model import model
from moong_model import model_2
from masur_model import model_3
from cauliflower_model import model_4

models_dict = {
    "bajra": model,
    "moong": model_2,
    "masur": model_3,
    "cauliflower": model_4
}

with open("./all_crop_models.pkl", "wb") as f:
    pickle.dump(models_dict, f)

with open("./all_crop_models.pkl", "rb") as f:
    loaded_models = pickle.load(f)
    bajra_model = loaded_models["bajra"]
    moong_model = loaded_models["moong"]
    masur_model = loaded_models["masur"]
    cauliflower_model = loaded_models["cauliflower"]