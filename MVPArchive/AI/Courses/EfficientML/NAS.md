Neural Architecture Search


## Primitive Operations

- **Linear**: in_channels  = 8,  out_channels  = 16
-  **Normal Convolution**:  in_channels  = 8,  out_channels  = 16, groups=1
    - One convolution over all input channels producing all output channels.
    - Input: CxHxW, Filter: FxCxKxK, Output: FxHxW 
    - F Filters of size CxKxK
- **Depth-Wise Convolution**:  in_channels  = 8,  out_channels  = 8, groups=8 
    - Eight independent convolutions, each over one input channel producing one output channel.
    - Input: CxHxW, Filter: Cx1xKxK, Output: CxHxW
    - C Filters of size 1xKxK
    - Each filter is applied only to its corresponding input channel, producing an output for each channel separately.
- **Grouped Convolution**:  in_channels  = 8,  out_channels  = 16, groups=4
    - Four independent convolutions, each over 2 input channels (in_channels/groups) producing 4 output channels (out_channels/groups).
    - Input: CxHxW, Filter: F/G x C/G x KxK, Output: FxHxW
    - G groups of F/G filters of size C/G x KxK.
    - if groups == in_channels becomes Depth wise convolution
- **Point-Wise Convolution** (1x1 Convolution): in_channels  = 8,  out_channels  = 16, groups=1
	- Each filter performs a linear combination across the depth channels, effectively transforming the depth without changing the spatial dimensions.
	- Input: CxHxW, Filter: FxCx1x1, Output: FxHxW
    - F Filters of size 1xKxK
	


![](attachments/Pasted%20image%2020240706085357.png)


## Classical Building Blocks

### ResNet: Bottleneck block

![](attachments/Pasted%20image%2020240706091811.png)
![](attachments/Pasted%20image%2020240706091833.png)


### ResNeXt: Grouped Convolution

![](attachments/Pasted%20image%2020240706094241.png)


### MobileNet: Depthwise Convolutions

![](attachments/Pasted%20image%2020240706094933.png)


![](attachments/Pasted%20image%2020240706095006.png)

![](attachments/Pasted%20image%2020240706095024.png)

![](attachments/Pasted%20image%2020240706095047.png)

### ShuffleNet: 1x1 Group Conv & Channel shuffle

- Further reduce the cost by replacing 1x1 convolution with 1x1 group convolution.
- Exchange information across different groups via channel shuffle

![](attachments/Pasted%20image%2020240706095543.png)



## NAS

![](attachments/Pasted%20image%2020240706140336.png)

### Search Space

#### Cell-level Search Space


























