import torch
from torch.utils.data import Dataset, DataLoader

t1 = torch.tensor([1,2,3])
t2 = torch.randn(1,3)
t3 = torch.ones([2,2])

z = t1 + t2



class customDataset(Dataset):
    def __init__(self):
          self.data = torch.randn(100,10)
              
    def __len__(self):
          return len(self.data)

    def __getitem__(self,idx):
          return self.data[idx]


dataset = customDataset()
dataLoader = DataLoader(dataset, batch_size=32)



# neural network
import tourch.nn as nn
class SimpleNN(nn.Module):
  def __init__(self):
    super(SimpleNN, self).__init__()
    self.fc1 = nn.Linear(10,64)
    self.fc2 = nn.Linear(64,1)

  def forward(self,x):
    x = torch.relu(self.fc1(x))
    x = self.fc2(x)
    return x
model = SimpleNN()
# print(model)