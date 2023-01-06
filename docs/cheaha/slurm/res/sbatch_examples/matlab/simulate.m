function simulate( ...
    seed, ...
    number_of_rolls, ...
    input_filepath_csv, ...
    output_filepath_csv ...
)
    %{
    Takes a collection of dice rolls from csv input filepath. Each dice roll is
    of the form (quantity,size,modifier) and results in a size-sided die rolled
    quantity times, the results summed up, and modifier added to the total. For
    each dice roll the process is repeated number_of_rolls times to create a
    list of rolls (for downstream statistics).

    The net result is a list of lists of integers, which is then written to a
    csv output filepath, one list of integers per line.

    Seed is provided for reproducibility of random simulation.

    One roll of a set of dice, plus modifier, is set to 1 if less than 1.
    %}
    % Read input values
    t = readtable(input_filepath_csv);

    % Simulate
    roll_data = NaN(height(t), number_of_rolls);
    for row_index = 1:height(t)
        rng(seed);

        quantity = t{row_index, 1};
        size = t{row_index, 2};
        modifier = t{row_index, 3};

        % actually perform the rolls
        rolls = simulate_many_dice_rolls( ...
            number_of_rolls, ...
            quantity, ...
            size, ...
            modifier ...
        );
        roll_data(row_index, :) = rolls;
    end

    % Write output values
    t_out = array2table(roll_data);
    writetable(t_out, output_filepath_csv, "WriteVariableNames", false);
end


function rolls = simulate_many_dice_rolls( ...
    number_of_rolls, ...
    quantity, ...
    size, ...
    modifier ...
)
    %{
    Simulate rolling a set of dice many times.

    Returns a list of integers, one per roll.
    %}
    rolls = NaN(number_of_rolls, 1);
    for index = 1:number_of_rolls
        value = roll_dice(quantity, size, modifier);
        rolls(index) = value;
    end
end


function total = roll_dice(quantity, size, modifier)
    %{
    Simulate rolling a set of dice one time.

    If quantity is 2, size is 6 and modifier is 3, then in tabletop gaming notation
    this would roll 2d6+3, or two 6-sided dice and add 3 to the result.
    %}
    rolls = randi([1 size], [1 quantity]);
    total = sum(rolls) + modifier;
    total = max(1, total);  % roll may not be negative
end
