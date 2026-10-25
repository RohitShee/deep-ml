def dim_from_space(space : dict) -> int :
    dim = 1
    if space['type'] =='Box' :
        for x in space['shape'] :
            dim*=x
    else :
        dim = space['n']
    return dim

def auto_mlp_from_spaces(obs_space: dict, act_space: dict, hidden_layers: list) -> dict:
    """
    Automatically determine MLP architecture from environment space definitions.

    Args:
        obs_space: dict with 'type' and type-specific keys defining the observation space
        act_space: dict with 'type' and type-specific keys defining the action space
        hidden_layers: list of ints specifying hidden layer widths

    Returns:
        dict with keys:
          'input_dim': int
          'output_dim': int
          'layer_shapes': list of ((weigh
          t_rows, weight_cols), (bias_dim,)) tuples
          'total_params': int
    """
    input_dim =dim_from_space(obs_space)
    output_dim = dim_from_space(act_space)
    total_params = 0
    layer_shapes = []
    curr = input_dim
    for layer in hidden_layers :
        layer_shapes.append(((curr,layer),(layer,)))
        total_params+=curr*layer+layer
        curr = layer
    layer_shapes.append(((curr,output_dim),(output_dim,)))
    total_params+=curr*output_dim+output_dim
    return {
        'input_dim' : input_dim,
        'output_dim' : output_dim,
        'layer_shapes' : layer_shapes,
        'total_params' : total_params
    }
    pass