# api package

This package provides an interface for communicating with the user.

Api provides 8 endpoints. 

- **KNN Endpoint** - /knn/host/ip range/view/k/t . Details are in documentation of a get method in knn_api class.
- **LOF Endpoint** - /lof/host/ip range. Details are in a documentation of a get method in lof_api class.
- **Range Endpoint** - /range/host/t. Details are in a documentation of a get method in range_api class.
- **Detail Endpoint** - /detail/host. Details are in a documentation of a get method in detail_api class.
- **LOF Range Endpoint** - /lof/range/ip range. Detils are in a documentation of a get method in lof_range_api class.
- **LOF Inter Range Endpoint** - /lof/interrange/source IP range/ target IP range. Details are in a documentation of a get method in lof_interrange_api class.
- **Scan Endpoint** - /scan/ip range. Details are in a documentation of a get method in scan_api class.
- **Quantiles Endpoint** - /quantiles/ip range. Details are in a documentation of a get method in quantiles_api class.