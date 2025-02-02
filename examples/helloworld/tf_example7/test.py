from neural_compressor import Metric
from neural_compressor.config import PostTrainingQuantConfig
from neural_compressor.data import DataLoader
from neural_compressor.data import Datasets
from neural_compressor.quantization import fit


def main():

    # Built-in dummy dataset
    dataset = Datasets('tensorflow')['dummy'](shape=(1, 224, 224, 3))
    # Built-in calibration dataloader and evaluation dataloader for Quantization.
    dataloader = DataLoader(framework='tensorflow', dataset=dataset)
    # Post Training Quantization Config
    config = PostTrainingQuantConfig()
    # Built-in topk metric
    top1 = Metric(name="topk", k=1)
    # Just call fit to do quantization.
    q_model = fit(model="./mobilenet_v1_1.0_224_frozen.pb",
                  conf=config,
                  calib_dataloader=dataloader,
                  eval_dataloader=dataloader,
                  eval_metric=top1)


if __name__ == "__main__":
    main()
