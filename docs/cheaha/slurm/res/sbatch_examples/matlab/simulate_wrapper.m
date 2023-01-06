function simulate_wrapper(varargin)
    %{
    Wrapper for use of simulate() in MATLAB batch mode, e.g., with SLURM.
    %}
    assert(nargin == 4);

    seed = str2double(varargin{1});
    number_of_rolls = str2double(varargin{2});
    input_filepath_csv = varargin{3};
    output_filepath_csv = varargin{4};

    simulate(seed, number_of_rolls, input_filepath_csv, output_filepath_csv);
end