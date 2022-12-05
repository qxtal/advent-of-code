# This was my first solution, but I realized that it was way
# overkill. I went with a simpler route, but I don't wanna
# throw this code away, so here it is, just sitting there.

def parse_crates_to_stacks__overkill(cr_input):
    # First, we convert the lines to a 2D array.
    # We save that array to a buffer.
    crates_buffer = []
    for line in cr_input:
        crates_buffer.append(list(line))
    
    # This is the hacky part. This will "rotate" the 2D array,
    # so that we can read each stack from left to right, instead
    # of bottom to top.
    #     Relevant SO entry: https://stackoverflow.com/a/8421412
    rotation_buffer = list(zip(*crates_buffer[::-1]))
    
    # Then we convert each line to an array of characters,
    # turning this back into a 2D array, but fully rotated.
    crates_text_parsed = []
    for line in rotation_buffer:
        crates_text_parsed.append(list(line))
    
    crate_stacks = []
    for line in crates_text_parsed[1::4]:
        stack = []
        for c in line[1::]:
            if c.isalpha():
                stack.append(c)
        crate_stacks.append(stack)

    return crate_stacks
