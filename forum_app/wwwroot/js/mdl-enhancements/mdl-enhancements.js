(function() {
    'use strict';

    MaterialDataTable.prototype.createCheckbox_ = function(row, opt_rows) {
      var label = document.createElement('label');
      var labelClasses = [
        'mdl-checkbox',
        'mdl-js-checkbox',
        'mdl-js-ripple-effect',
        this.CssClasses_.SELECT_ELEMENT
      ];
      label.className = labelClasses.join(' ');
      var checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.classList.add('mdl-checkbox__input');

      if (row) {
        // Enhancement 
        // We add a data-record attribute on the <tr> tag and assign it as the checkbox value
        checkbox.value = row.dataset['record'];

        checkbox.checked = row.classList.contains(this.CssClasses_.IS_SELECTED);
        checkbox.addEventListener('change', this.selectRow_(checkbox, row));
      } else if (opt_rows) {
        checkbox.addEventListener('change', this.selectRow_(checkbox, null, opt_rows));
      }
  
      label.appendChild(checkbox);
      componentHandler.upgradeElement(label, 'MaterialCheckbox');
      return label;
    };
  
  // EXAMPLE POC of enhancing MaterialDataTable
  // https://github.com/google/material-design-lite/blob/60f441a22ed98ed2c03f6179adf460d888bf459f/src/data-table/data-table.js#L115
  // MaterialDataTable.prototype.Konstant = {
  //   // None at the moment.
  //   X : 122
  // };
})();