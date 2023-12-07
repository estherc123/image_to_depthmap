# Final Project for CS182
The majority of our code and our base model are taken from https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix.git
We modified the code such that there's an option to finetune with LoRA.
This project is a model finetuned on a pre-trained pix2pix model. It takes an RGB image and converts it into a RGB color-coded depth map.

We used this Google Colab notebook: https://colab.research.google.com/drive/1MGQR-uSnoEb3UZiQNnkDUHyf-0S39rHy?usp=sharing for fine-tuning and testing.

# Finetune
To finetune, first run `python finetune_no_lora.py --dataroot /path/to/train/data --name img2depthmap --model pix2pix  --n_epochs 2 --n_epochs_decay 0 --direction AtoB --lora_rank {NUM LORA RANK, 0 MEANS NO LORA}`
Then delete `latest_net_G.pth` in folder `checkpoint`, and move the model you want to finetune to folder `checkpoint`, rename it `latest_net_G.pth`.

After that, run `python finetune_no_lora.py --dataroot /path/to/train/data --name img2depthmap --model pix2pix --continue_train  --n_epochs {NUM EPOCH} --n_epochs_decay 0 --direction AtoB --lora_rank 16`

# Test
Be sure /path/to/test/data contains folder `test`.
Then run `python test.py --dataroot /path/to/test/data --name img2depthmap --model pix2pix --direction AtoB`.
